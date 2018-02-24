from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from ipaddress import ip_address, ip_network

# Create your views here.

@csrf_exempt
def hello(request):
    # Verify if request came from GitHub
    print("hello")
    print(request)
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    print(request.META)
    client_ip_address = ip_address(forwarded_for)
    print(client_ip_address)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    return HttpResponse('pong')
