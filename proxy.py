import requests
import json


def proxy_api():
    url = 'http://pubproxy.com/api/proxy?type=https'  # url – просто строка с запросом
    response = requests.get(url)
    proxy = json.loads(response.text)
    ip = proxy["data"][0]['ipPort']
    return ip
