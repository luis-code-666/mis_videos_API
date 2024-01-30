from fastapi import FastAPI, Body,Path, Query 
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional


# uvicorn main:app --reload --port 5000 --host 0.0.0.0
# la palabra --reload es para que se recarge automaticamente
# la palabra --port 5000 es por el puero que quieres que escuche el navegador 
# la palabra --host 0.0.0.0 es para que se comunique desde cualquier dispositivo 


#esto es para cambiar el nombre de lo que sale en la pantalla de docs
#parametro por ruta 
app = FastAPI()
app.title = "Mi aplicacion con FastAPI" #para cambiar el nombre
app.version = "0.0.1" #para cambiar la version 

class Movie(BaseModel):
    id: Optional[int] = None
    #como poner su default en la logica
    #title: str = Field(default="Mi pelicula", min_length=5, max_length=15)
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)
    
    class Config:
        # se declara ahi con json para que pueda jalar loq ue se esta escribiendo 
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "secription de la pelicula",
                "year": 2022,
                "rating": 9.8,
                "category": "Accion"
            }
        }
    
    
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
#,etodo PATH es para validad los parametros de ruta para en las funciones 
def get_movies_(id: int = Path(ge=1, le=2000)):
    #para el filtrado de las peliculas 
    for item in movies:
        if item["id"] == id:
            return item
    return []

#filtrado de peliculas por su categoria 
@app.get('/movies/', tags=['movies'])
# def get_movies_by_category(category:str, year:int):
#validaciones de los parametros 
def get_movies_by_category(category:str = Query(min_length=5, max_length=15)):
    return [item for item in  movies if item['category'] == category ]
    #return category

@ app.post('/movies/', tags=['movies'])
def create_movies(movie:Movie):
# def create_movies(id:int = Body(), title: str = Body(), overview:str = Body(), year:int = Body(), rating:str = Body(), category:str = Body()):
    movies.append(movie)
    '''movies.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })'''
    return movies
#esto es para actualizar o editar datos 
@app.put('/movies/{id}', tags=['movies'])
# def update_movies(id:int, title: str = Body(), overview:str = Body(), year:int = Body(), rating:str = Body(), category:str = Body()):
def update_movies(id:int, movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return movies
        
#para eliminar parametros 
@app.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies
