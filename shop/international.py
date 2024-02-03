from country_languages import country_languages
from deep_translator import GoogleTranslator
import requests as R

def ip_to_countryName(ip):
        ''' Find country name from ip address '''
        response = R.get(f'https://freeipapi.com/api/json/{ip}')
        data = response.json()
        countryName = data['countryName']
        return countryName

def countryLanguage(countryName):
    ''' find country language code from country name '''
    language_code = country_languages[countryName] if countryName in country_languages else 'en'
    return language_code

