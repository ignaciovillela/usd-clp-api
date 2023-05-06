import json
from _decimal import ROUND_HALF_UP
from decimal import Decimal

import requests
from cachetools.func import ttl_cache
from django.http import JsonResponse

URL = 'https://v6.exchangerate-api.com/v6/534569873736672ef33d04ea/latest/{_from}'


@ttl_cache(ttl=600)
def from_to_conversion(from_currency, to_currency):
	response = requests.get(URL.format(_from=from_currency.upper()))
	return json.loads(response.content)['conversion_rates'][to_currency.upper()]


def conversor(request, amount=Decimal(1), from_currency='usd', to_currency='clp'):
	exchange_factor = Decimal(from_to_conversion(from_currency, to_currency))
	value = amount * exchange_factor
	rounded_value = value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP)
	return JsonResponse({'value': float(rounded_value)})
