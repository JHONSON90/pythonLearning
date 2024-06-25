from fastapi import APIRouter

#utilizamos el prefijo para no estar escribiendo en todas los paths "/products/"

router = APIRouter( prefix="/products",
                    tags= ["products"], #para la documentacion separa por products y genera documentacion para products
                    responses={404: {"message": "No Encontrado"}}) 


product_list=["producto 1","Producto 2", "Producto 3"]

@router.get("/") #aqui ya evitamos escribir products ya el sistema entiende que es /products
async def products():
    return product_list

@router.get('/{id}')
async def products(id: int):
    return product_list[id]

# TODO: CREAR TAGS PARA USERS Y COLOCAR LOS ERRORES EN TODAS LAS QUERYS QUE SE EJECUTEN