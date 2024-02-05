from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from deep_translator import GoogleTranslator
from requests.auth import HTTPBasicAuth
from django.http import JsonResponse
from django.shortcuts import render
from ipaddr import client_ip
from .models import Products
import requests


def index(request):
    pro = Products.objects.all()
    return render(request, 'index/index.html', {'products': pro})

def insert_products(request):
    url = '*'
    consumer_key = '*'
    consumer_secret = '*'
    
    # Set up authentication
    auth = HTTPBasicAuth(consumer_key, consumer_secret)

    id_list = []

    for i in range(1, 5, 1):
        response = requests.get(f'{url}/products', params={'page': {i}, 'per_page': 100}, auth=auth)
        products = response.json()
        len_data = len(products)
        for j in range(len_data):
            if products[j]["on_sale"] and products[j]["type"] == 'variable':
                id_list.append(products[j]["id"])
                    

    for x in id_list:
        r = requests.get(f'{url}/products/{x}/variations', auth=auth)
        product = r.json()
        if int(product[0]["stock_quantity"]) > 0 :
            Products.objects.create(
                product_id = product[0]["id"],
                product_sku = product[0]["sku"],
                product_regular_price = product[0]["regular_price"],
                product_price = product[0]["price"],
                product_image = product[0]["image"]["src"],
                product_permalink = product[0]["permalink"] + "?utm_source=GoogleAds&utm_medium=123kifCOM&utm_campaign=nowruz&utm_term=123KIF&utm_content=Products",
            )

    return render(request, 'index/index.html')