from fastapi import FastAPI, Body
from urllib.parse import unquote
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    state: str
    id_token: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/')
async def root(id_token: Optional[str] = Body(None), state: Optional[str] = Body(None)):
    print(id_token, state)
    return id_token


@app.get("/launch")
async def launch(iss, login_hint, target_link_uri, lti_message_hint):
    print(f"ISS is {iss}")
    print(f"Login hint is {login_hint}")
    print(f"Target link uri is {target_link_uri}")
    print(f"lti_message_hint is {lti_message_hint}")
    return {'iss':iss, 
            'login_hint':login_hint,
            'target_link_uri':target_link_uri,
            'lti_message_hint':lti_message_hint}
    
