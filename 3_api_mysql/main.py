#levanta el servidor y carga el fichero de rutas
from fastapi import FastAPI
from routes import product_routes, user_routes, auth_routes

app=FastAPI()
app.include_router(product_routes.router,
                   prefix="/products",
                   tags=["Products"])

app.include_router(user_routes.router,
                   prefix="/users",
                   tags=["Users"])

app.include_router(auth_routes.router,
                   prefix="/auth",
                   tags=["Auth"])