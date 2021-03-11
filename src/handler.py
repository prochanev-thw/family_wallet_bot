import os
import json
import requests
from pprint import pprint

def handler(event, context):

    response = requests.get('https://api.ipify.org/?format=json').json()

    return {'ip': response}
