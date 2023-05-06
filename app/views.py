import json
from math import ceil

import requests
from django.http import JsonResponse

URL = 'https://v6.exchangerate-api.com/v6/534569873736672ef33d04ea/latest/USD'


def usd_to_clp(usd):
	response = requests.get(URL)
	return usd * json.loads(response.content)['conversion_rates']['CLP']


def dollar(request, usd=1):
	clp = usd_to_clp(usd)
	ceil_clp = ceil(clp)
	data = {'clp': ceil_clp}
	if request.GET.get('display'):
		data['display'] = f'$ {ceil_clp:,.2f}'.replace(',', ';').replace('.', ',').replace(';', '.')
	return JsonResponse(data)
