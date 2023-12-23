from fastapi import FastAPI
from fastapi.responses import HTMLResponse


# uvicorn main:app --reload --port 5000 --host 0.0.0.0
# la palabra --reload es para que se recarge automaticamente
# la palabra --port 5000 es por el puero que quieres que escuche el navegador 
# la palabra --host 0.0.0.0 es para que se comunique desde cualquier dispositivo 


#esto es para cambiar el nombre de lo que sale en la pantalla de docs

app = FastAPI()
app.title = "Mi aplicacion con FastAPI" #para cambiar el nombre
app.version = "0.0.1" #para cambiar la version 

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "override": "es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2019",
        "rating": 7.8,
        "category": "Accion"
    }
]

@app.get('/', tags=['home'])
def message():
    #return "Hello, world!"
    return HTMLResponse('<h1> Hello, world!</h1>')

@app.get('/movies/', tags=['movies'])
def get_movies():
    return movies