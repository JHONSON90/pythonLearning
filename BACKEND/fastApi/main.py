from fastapi import FastAPI
from routers import products, users, users_db
#! importamos para traer recursos staticos
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#? importacion de rutas
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)

#? montar recursos estaticos
app.mount("/static", StaticFiles(directory='static'), name="static")



@app.get("/") 
async def root(): # siempre que llamamos a un servidor la peticion siempre sera asincrona lo que quiere decir que la app no hace nada hasta que el servidor envie una respuesta
    return "message: Hello World"


##! vamos a levantar el servidor
 # uvicorn main:app --reload
 
@app.get('/url')
async def url():
    return {"url_curso": "https://mouredev.com/python"}