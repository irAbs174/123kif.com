from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from deep_translator import GoogleTranslator
from django.http import JsonResponse
from django.shortcuts import render
from ipaddr import client_ip


def index(request):
    return render(request, 'index/index.html')

def translate(language_code, text):
    ''' give a text and return  '''
    translated = GoogleTranslator(source='auto', target=f'{language_code}').translate(text=f"{text}")
    return translated
