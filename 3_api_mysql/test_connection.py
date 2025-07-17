from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv #carga las variables del fichero .env
import aiomysql
import os # operating system me va a permitir acceder a archivos y carpetas 


app= FastAPI()
load_dotenv()

#creacion del modelo en base a nustra BBDD
class Product(BaseModel):
    id:int
    title:str
    price:float
    quantity:int
    status:int



#conexion a BBDD usando el fichero .env - libreria .env de python

#creamos una funcion asincrona
async def get_connection(): 
    return await aiomysql.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        db=os.getenv("MYSQL_DATABASE")
    )

@app.get('/')
def init():
    return 'conexion iniciada con el servidor'

@app.get('/products', status_code=200)
async def get_all_products():
    #obtener acceso a la base de datos asincrona
    conn=await get_connection()
    #situo el cursor al final de la tabla para consultar todos los datos de la misma.Una funcion que llamo cursor
    async with conn.cursor(aiomysql.DictCursor) as cursor:
        await cursor.execute('SELECT * FROM upgrade_shop.products')
        #obtener los resultados
        data= await cursor.fetchall()
    conn.close()
    return data