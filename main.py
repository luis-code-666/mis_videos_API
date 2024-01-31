from fastapi import FastAPI, Body,Path, Query 
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List


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
                "overview": "Description de la pelicula",
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
# colocando los codigos de eroor de 200, 300, 400, 500
@app.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200)
#esa list se puede colocar en la funcion que se puede devollver
def get_movies() -> List[Movie]:
    return JSONResponse(status_code=200, content=[movies])

#con parametro por ruta
@app.get('/movies/{id}', tags=['movies'], response_model=Movie, status_code=200)
#,etodo PATH es para validad los parametros de ruta para en las funciones 
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    #para el filtrado de las peliculas 
    for item in movies:
        if item["id"] == id:
            return JSONResponse(status_code=200, content=item)
    return JSONResponse(status_code=404, content=[])

#filtrado de peliculas por su categoria 
@app.get('/movies/', tags=['movies'], response_model=List[Movie], status_code=200)
# def get_movies_by_category(category:str, year:int):
#validaciones de los parametros 
def get_movies_by_category(category:str = Query(min_length=5, max_length=15)) -> List[Movie]:
    data = [item for item in  movies if item['category'] == category ]
    return JSONResponse(status_code=200, content=[data])
    #return category

@ app.post('/movies', tags=['movies'], response_model=dict, status_code=201)
def create_movie(movie:Movie) -> dict:
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
    return JSONResponse(status_code=201, content={"menssage":"Se ha registrado la pelicula"})
#esto es para actualizar o editar datos 
@app.put('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
# def update_movies(id:int, title: str = Body(), overview:str = Body(), year:int = Body(), rating:str = Body(), category:str = Body()):
def update_movies(id:int, movie:Movie) -> dict:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category'] = movie.category
            return JSONResponse(status_code=200, content={"menssage":"Se ha modificado la pelicula"})
        
#para eliminar parametros 
@app.delete('/movies/{id}', tags=['movies'], response_model=dict, status_code=200)
def delete_movies(id: int)-> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={"menssage":"Se ha eliminado la pelicula"})
