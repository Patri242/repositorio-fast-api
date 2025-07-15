#levanta el servidor y carga el fichero de rutas
from fastapi import FastAPI
from routes import product_routes

app=FastAPI()
app.include_router(product_routes.router,
                   prefix="/products",
                   tags=["Products"])