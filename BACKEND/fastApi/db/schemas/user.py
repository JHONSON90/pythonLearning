# nos sirve para interpretar los modelos que estamos manejando osea que solicitamos informacion qeu nos va a llegar en un json y lo necesitamos mirar como un objeto

def user_schema(user) -> dict:
      return{
       "id": str(user["_id"]),
       "username": user["username"],
       "email": user["email"]
   }

    
    
