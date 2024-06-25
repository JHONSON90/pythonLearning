from fastapi import APIRouter, status, Response 
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter( prefix='/user',
                 tags=['user'],
                 responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

@user.get('/', response_model=list[User], status_code=status.HTTP_202_ACCEPTED, tags=["users"])
def find_all_users():
    return usersEntity(conn.local.user.find())

@user.get('/{id}', response_model=User, status_code=status.HTTP_202_ACCEPTED,tags=["user"])
def find_user(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.post('/', response_model=User, status_code=status.HTTP_202_ACCEPTED,tags=["user"])
def crate_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"]) #encripta las contraseñas
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    
    user = conn.local.user.find_one({"_id":id})
    return userEntity(user)
    

@user.put('/{id}', response_model=User, status_code=status.HTTP_202_ACCEPTED,tags=["user"])
def update_user(id:str, user:User):
    conn.local.user.find_one_and_update({
        "_id" : ObjectId(id)
        }, {
            "$set": dict(user)
        })
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,tags=["user"])
def delete_user(id: str):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)