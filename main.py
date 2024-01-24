from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import baseModel


# uvicorn main:app --reload --port 5000 --host 0.0.0.0
# la palabra --reload es para que se recarge automaticamente
# la palabra --port 5000 es por el puero que quieres que escuche el navegador 
# la palabra --host 0.0.0.0 es para que se comunique desde cualquier dispositivo 


#esto es para cambiar el nombre de lo que sale en la pantalla de docs
#parametro por ruta 
app = FastAPI()
app.title = "Mi aplicacion con FastAPI" #para cambiar el nombre
app.version = "0.0.1" #para cambiar la version 

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2019",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "es un exuberante planeta llamado Pandora viven los Na'vi",
        "year": "2019",
        "rating": 7.8,
        "category": "Accion"
    }
]

@app.get('/', tags=['home']) #pertenece a home
def message():
    #return "Hello, world!"
    return HTMLResponse('<h1> Hello, world!</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

#con parametro por ruta
@app.get('/movies/{id}', tags=['movies'])
def get_movies_(id: int):
    #para el filtrado de las peliculas 
    for item in movies:
        if item["id"] == id:
            return item
    return []

#filtrado de peliculas por su categoria 
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category:str, year:int):
    #return [item for item in  movies if item['category'] == category ]
    return category

@ app.post('/movies/', tags=['movies'])
def create_movies(id:int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating:str = Body(), category:str = Body()):
    movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies
#esto es para actualizar o editar datos 
@app.put('/movies/{id}', tags=['movies'])
def update_movies(id:int, title: str = Body(), overview:str = Body(), year:int = Body(), rating:str = Body(), category:str = Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category
            return movies
        
#para eliminar parametros 
@app.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies
