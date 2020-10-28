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

        print(login_hint, lti_message_hint, target_link_uri)
        #
        print(
            ge('auth_endpoint'), 
            {'login_hint':login_hint, 
            'lti_message_hint':lti_message_hint,
            'client_id':APP_ID,
            'nonce':"fc5fdc6d-5dd6-47f4-b2c9-5d1216e9b771",
            'redirect_uri':target_link_uri,
            'response_type':'id_token',
            'scope':'openid',
            'state':'a unique value'})
        
    else:
        wp.add(jp.P(text="NO QUERY PARAMS"))
    
    wp.add(jp.P(text=f"Working it out"))
    
    if resp.status_code == 200:
        wp.add(jp.P(text="{resp.text}"))
    """
    https://bbtest2.cc.ku.edu/webapps/blackboard/execute/blti/launchPlacement?cmd=authenticate&
    client_id=8b391e79-ab66-4f8a-9fa2-027782f7a598&
    login_hint=https%253A%252F%252Fbbtest2.cc.ku.edu%252Fwebapps%252Fblackboard%252Fexecute%252Fblti%252FlaunchPlacement%253Fcmd%253Dauthenticate%2C884f23954de74294bff1ab9d1a8a43a7&
    lti_message_hint=eyJmcm9tVWx0cmEiOmZhbHNlLCJwb3NpdGlvbiI6LTEsInRhcmdldExpbmtVcmwiOiJodHRwczovL2JibHRpLmhlcm9rdWFwcC5jb20iLCJwbGFjZW1lbnRJZCI6Il8zNjRfMSIsInRhcmdldE92ZXJyaWRlIjpudWxsLCJmcm9tR3JhZGVDZW50ZXIiOmZhbHNlLCJvcGVuTmV3V2luZG93IjpmYWxzZSwiZGVlcExpbmtMYXVuY2giOnRydWUsImNvdXJzZUlkIjoiXzIzNzYxNV8xIiwiY29udGVudElkIjoiXzYyMDg0M18xIn0%3D&nonce=fc5fdc6d-5dd6-47f4-b2c9-5d1216e9b771
    &redirect_uri=https%3A%2F%2Fbbltiapi.herokuapp.com%2F
    &response_type=id_token
    &scope=openid
    &state=a%20unique%20value
    """
    return wp
   

@jp.SetRoute('/')
async def main(request):
    print(request)
    wp = jp.WebPage()
    wp.add(jp.P(text='This is the main page'))
    return wp

jp.justpy(start_server=False)
