from fastapi import FastAPI


# uvicorn main:app --reload --port 5000 --host 0.0.0.0
# la palabra --reload es para que se recarge automaticamente
# la palabra --port 5000 es por el puero que quieres que escuche el navegador 
# la palabra --host 0.0.0.0 es para que se comunique desde cualquier dispositivo 
app = FastAPI()
@app.get('/')

def message():
    return "Hello, world!"