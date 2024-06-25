from fastapi import APIRouter, HTTPException, status

#importamos la clase de Usuario que tenemos creada

from db.models.user import User

#! importamos la conexion 
from db.client import db_client

#importamos el esquema
from db.schemas.user import user_schema

router = APIRouter( prefix='/userdb',
                   tags=['userdb'],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


# para levantar el servidor en este archivo seria uvicorn users:app --reload

users_list = []


#! vamos a ver Post que nos sirve para crear datos

@router.post("/", response_model= User, status_code=status.HTTP_201_CREATED) # se puede colocar de una vez el codigo de respuesta en caso de que salga bien
async def user(user: User):
    
    # if type(search_user_by_email("email", user.email)) == User:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario ya existe") #raise nos sirve para retornarlo como codigo de status y ya nos maneja el error       
          
    user_dict = dict(user)
    print(user_dict)
    return "recived"
    #del user_dict["id"] # eliminamos el id del user_dict para que mongo lo coloque automaticamente
    
    #id = db_client.local.users.insert_one(user_dict)
    
    #new_user = user_schema(db_client.local.users.find_one({"_id":id}))
    
    #return User(**new_user)







@router.get("/")
async def usersclass():
    return users_list

#LLAMADOS POR EL PATH! osea que estan en la url 

@router.get("/{id}")
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
    
    
    
#! Vamos a crear un put para modificar 
@router.put("/")
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

@router.delete("/{id}")
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


def search_user_by_email(email: str):
    try:
        user =  db_client.local.user.find_one({"email":email})
        return User(user_schema(**user))
    except:
        return {"Error": "El usuario no ha sido encontrado"}
    
