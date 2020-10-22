from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/launch")
async def launch(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
    return kwargs

