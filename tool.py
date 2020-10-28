import justpy as jp
from os import getenv as ge
from dotenv import load_dotenv
import requests

app = jp.app
BACKEND_URL = ge('backend')
APP_ID = ge('appid')

load_dotenv()
session_data={}

@jp.SetRoute('/hello')
async def hello(request):
    wp = jp.WebPage()
    wp.add(jp.P(text='Hello there!', classes='text-5xl m-2'))
    wp.add(jp.P(text=f"APP ID is {ge('appid')}"))
    return wp

@jp.SetRoute('/launch')
async def launch(request):
    wp = jp.WebPage()
    url = ''
    print(APP_ID)
    if len(request.query_params) > 0:
        login_hint = request.query_params['login_hint']
        lti_message_hint = request.query_params['lti_message_hint']
        target_link_uri = request.query_params['target_link_uri']

        token = requests.get(f"{BACKEND_URL}launch", params=request.query_params).json()
        wp.add(jp.P(text=f"{token}"))
        
    else:
        wp.add(jp.P(text="NO QUERY PARAMS"))

    return wp
   

@jp.SetRoute('/')
async def main(request):
    print(request)
    wp = jp.WebPage()
    wp.add(jp.P(text='This is the main page'))
    return wp

jp.justpy(start_server=False)
