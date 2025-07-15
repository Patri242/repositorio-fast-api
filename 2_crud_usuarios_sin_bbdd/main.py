from fastapi import FastAPI
from routes import user_routes #1º importar 

app = FastAPI()
app.include_router(
    user_routes.router,
    prefix= "/users",#los dos primeros son los mas importantes
    tags = ['users'] #crear un fichero por cada 1 de las entidades

)