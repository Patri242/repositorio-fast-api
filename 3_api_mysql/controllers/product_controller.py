from db.config import get_connection
from fastapi import HTTPException
from models.product_model import Product
import aiomysql

async def get_products_list():
    try:
        #obtenemos acceso a la base de datos
        conn= await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            #consultamos los datos
            await cursor.execute('SELECT * FROM upgrade_shop.products')
            #obtener los resultados
            data= await cursor.fetchall()
        conn.close()
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de MYSQL: {str(e)}")
    
async def obtener_por_id(id_product):
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            # OJO await cursor.execute(f'SELECT * FROM upgrade_shop.products WHERE id={id_product}')
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE id=%s',(id_product,)) 
            #tupla. lista inmutable. no me pueden hacer una inyeccion q no quiera
            data=await cursor.fetchone() #fetchall para muchos y fetchone para 1
        conn.close()
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='Producto no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de MYSQL: {str(e)}")
    

#practicar. una ruta que me permita sacar uno o varios productos por precio min y precio max

async def obtener_por_precio(min_price, max_price):
    try:
        conn=await get_connection() #abrimos conexion
        async with conn.cursor(aiomysql.DictCursor) as cursor: #coloca el cursor abajo
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE price between %s and %s',(min_price, max_price))
            data= await cursor.fetchall()
        conn.close()
        if data:
            return data
        else:
            raise HTTPException(status_code=404 , detail='Producto no encontrado')
    except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error de MYSQL: {str(e)}")


#una ruta que me permita sacar un producto por su titulo. deberá devolverme listado de productos
async def obtener_por_titulo(title):
    try:
        conn = await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            query = 'SELECT * FROM upgrade_shop.products WHERE LOWER(title) LIKE %s'
            value = f"%{title.lower()}%"
            await cursor.execute(query, (value,))
            data = await cursor.fetchall()
        conn.close()
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='Producto no encontrado')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error mysql {str(e)}')
    

#una ruta que me permita devolver un listado de productos que no esten en stock.status:1
async def obtener_por_stock():
    try:
        conn = await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE status= 0')
            data = await cursor.fetchall()
        conn.close()
        if data:
            return data
        else:
            raise HTTPException(status_code=404 , detail='Producto no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de MYSQL: {str(e)}")
    
#una ruta que me permita devolver un listado de productos con cantidad mayor de 10

async def obtener_por_cantidad():
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE quantity > 10')
            data = await cursor.fetchall()
        conn.close()
        if data:
            return data
        else:
            raise HTTPException(status_code=404 , detail='Producto no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de MYSQL: {str(e)}")