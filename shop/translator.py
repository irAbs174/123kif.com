#from .models import ()
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from deep_translator import GoogleTranslator
from django.http import JsonResponse
from ipaddr import client_ip
import requests as R

#51.15.212.225 34.34.153.112
def ip_to_countryName(ip):
    # Find request country from ip address
    response = R.get(f'https://freeipapi.com/api/json/{ip}')
    data = response.json()
    print(data)
    countryName = data['countryName']
    translated = GoogleTranslator(source='auto', target='de').translate(text="سلام")
    print(translated)
    return countryName

ip_to_countryName("34.34.153.112")
