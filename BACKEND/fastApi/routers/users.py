from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


# para levantar el servidor en este archivo seria uvicorn users:app --reload
@router.get("/usersjson")
async def usersjson():
    return [{"name": "Jhon", "surName": "Portilla", "url": "https://moure.dev", "age": 25}, 
            {"name": "Edison", "surName": "Luna", "url": "https://edisonLuna.co", "age": 35},
            {"name": "Juan", "surName": "Caguazango", "url": "https://juancaguazango.dev", "age": 29},
            ]
    
# vamos a crear una entidad users

class User(BaseModel):
    name: str
    surname: str
    url:str
    age: int
    id: int
    
# con esto podemos pasar listas de usuarios de la siguiente manera

users_list = [User(name = "Jhon", surname="Portilla", url="http://Jhonson90.com", age=40, id=1), 
              User(name = "Edison", surname="Luna", url="https://edisonLuna.co", age=35, id=2),
              User(name = "Juan", surname="Caguazango", url="https://juancaguazango.dev", age=29,id=3),
              ]


@router.get("/users")
async def usersclass():
    return users_list

#LLAMADOS POR EL PATH! osea que estan en la url 

@router.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list ) ## funcion de orden superior 
    try:
        return list(users)[0]
    except:
        return {"Error": "El usuario no ha sido encontrado"}
    

#LLAMADOS POR QUERY! osea que estan en la url 

@router.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list ) ## funcion de orden superior 
    try:
        return list(users)[0]
    except:
        return {"Error": "El usuario no ha sido encontrado"}
    
    
#! vamos a ver Post que nos sirve para crear datos

@router.post("/user/", status_code=201, response_model= User) # se puede colocar de una vez el codigo de respuesta en caso de que salga bien
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe") #raise nos sirve para retornarlo como codigo de status y ya nos maneja el error
        
    else:
        users_list.append(user)
        return user
    
#! Vamos a crear un put para modificar 
@router.put("/user/")
async def user(user: User):
    found = False
    for index, save_user in enumerate(users_list):
        if save_user.id == user.id:
            users_list[index] = user
            found = True
            
        
    if not found:
        return{"error": "No se ha actualizado el usuario"}
    return user
            
#! eliminar un usuario para eliminar

@router.delete("/user/{id}")
async def user(id: int):
    try:
        found = False
        for index, save_user in enumerate(users_list):
            del users_list[index]
            found = True
            
        
        if not found:
            return {"error": "No se ha podido eliminar el usuario"}
    except:
        return {"Error": "El usuario no ha sido encontrado"}

#? vamos a crear una funcion que me haga la comprobacion y la vamos a utilizar en las funciones de arriba


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list )
    try:
        return list(users)[0]
    except:
        return {"Error": "El usuario no ha sido encontrado"}
    
