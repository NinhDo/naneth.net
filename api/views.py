import hmac
from hashlib import sha1

from decouple import config
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.encoding import force_bytes

import requests
from ipaddress import ip_address, ip_network
import subprocess

script_path = "/var/scripts/redeploy.sh"

# Create your views here.
@require_POST
@csrf_exempt
def hello(request):
    print(request.META)
    # Verify if request came from GitHub
    forwarded_for = u'{}'.format(request.META.get('REMOTE_ADDR'))
    forwarded_for2 = u'{}'.format(request.META.get('HTTP_X_REAL_IP'))
    client_ip_address = ""

    try:
        client_ip_address = ip_address(forwarded_for)
    except:
        client_ip_address = ip_address(forwarded_for2)

    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
    else:
        return HttpResponseForbidden('Permission denied.')

    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(config('GITHUB_WEBHOOK_KEY')), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    event = request.META.get('HTTP_X_GITHUB_EVENT', 'ping')
    if event == 'ping':
        return HttpResponse('pong')
    elif event == 'push':
        subprocess.call([script_path])
        return HttpResponse('success')

    return HttpResponse(status=204)
