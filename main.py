from fastapi import FastAPI, Form
from typing import Optional
from jose import jwt

import requests
from os import getenv as ge

app = FastAPI()

APPID = ge('appid')
KEY_SET_URL = ge('key_set_url')

print(f"AppId is {APPID}")
print(f"Key Set Url is {KEY_SET_URL}")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/')
async def root(id_token: Optional[str] = Form(...), state: Optional[str] = Form(...)):
    key_dict = requests.get(KEY_SET_URL).json()
    key = [key for key in key_dict['keys'] if key['kid'] == APPID][0]
    print(key)
    print(id_token)
    print(jwt.decode(id_token, key=key, audience=APPID))
    return id_token


@app.get("/launch")
async def launch(iss, login_hint, target_link_uri, lti_message_hint):
    resp = requests.get(
        ge('auth_endpoint'), 
        params={'login_hint':login_hint, 
                'lti_message_hint':lti_message_hint,
                'client_id':APPID,
                'nonce':"fc5fdc6d-5dd6-47f4-b2c9-5d1216e9b771",
                'redirect_uri':target_link_uri,
                'response_type':'id_token',
                'scope':'openid',
                'state':'a unique value '})
    
    print(resp.status_code)
    
