from fastapi import FastAPI, Header
from urllib.parse import unquote
from pydantic import BaseModel

app = FastAPI()



class Item(BaseModel):
    jwt: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/')
async def root(item: Item):
    print('Launched the application')
    print(item)
    return {'message':'What will happen?'}


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
    
