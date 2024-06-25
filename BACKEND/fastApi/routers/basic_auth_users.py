#vamos a autenticar usuarios

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

# estancia de oauth2
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool
    
class UserDB(User):
    password: str

users_db = {
    "jhonson":{
            "username": "jhonson",
            "full_name": "Jhon Edison Portilla Luna",
            "email": "Jportilla14@estudiantes.areandina.edu.co",
            "disabled": False,
            "password": "123456789"
    },
        "mouredev":{
            "username": "mouredev",
            "full_name": "Jhon Edison Portilla Luna",
            "email": "Jportilla14@estudiantes.areandina.edu.co",
            "disabled": True,
            "password": "1234567890"
    }
    
}

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username]) #estamos buscando en la base de datos un usuario y lo creamos en la base de datos

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
    
# configurando la dependencia

async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail="Credenciales de autenticacion invalidas", 
                headers={'www-Authenticate': 'Bearer'}
            )
    if user.disabled:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Usuario inactivo", 
                headers={'www-Authenticate': 'Bearer'}
        )
    return user
        

    
# vamos hacer la autenticacion del usuario y su contraseña
@app.post('/login')
async def login(form: OAuth2PasswordRequestForm = Depends()):
    #comprobando si hay un usuario
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto"
        )
        
    user = search_user_db(form.username)
    if not form.password == user.password:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta"
        ) 
         
    return {"access_token": user.username,"token_type" : "bearer" }

#aqui entra la dependencia de que si el usuario ya esta autenticado
@app.get('/users/me')
async def me(user: User = Depends(current_user)):
    return user