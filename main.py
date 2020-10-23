from fastapi import FastAPI, Form
from urllib.parse import unquote
from pydantic import BaseModel
from typing import Optional
from jose import jwt

import requests
from os import getenv as ge

app = FastAPI()

class Item(BaseModel):
    state: str
    id_token: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/')
async def root(id_token: Optional[str] = Form(...), state: Optional[str] = Form(...)):
    return {'jwt':id_token}


@app.get("/launch")
async def launch(iss, login_hint, target_link_uri, lti_message_hint):
    resp = requests.get(
        ge('auth_endpoint'), 
        params={'login_hint':message_params['login_hint'], 
                'lti_message_hint':message_params['lti_message_hint'],
                'client_id':ge("appid"),
                'nonce':"fc5fdc6d-5dd6-47f4-b2c9-5d1216e9b771",
                'redirect_uri':message_params['target_link_uri'],
                'response_type':'id_token',
                'scope':'openid',
                'state':'a unique value '})
    


    key_dict = requests.get(ge('key_set_url')).json()
    key = [key for key in key_dict['keys'] if key['kid'] == ge('appid')][0]
    
    token = resp.json()['jwt']

    return jwt.decode(token, key=key, audience=ge('appid'))
    
