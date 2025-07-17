from db.config import get_connection
from fastapi import HTTPException
from models.product_model import Product, ProductCreate
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
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()
    
async def obtener_por_id(id_product):
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            # OJO await cursor.execute(f'SELECT * FROM upgrade_shop.products WHERE id={id_product}')
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE id=%s',(id_product,)) 
            #tupla. lista inmutable. no me pueden hacer una inyeccion q no quiera
            data=await cursor.fetchone() #fetchall para muchos y fetchone para 1
        if data:
            return data
        else:
            raise HTTPException(status_code=404, detail='Producto no encontrado')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()
    

#practicar. una ruta que me permita sacar uno o varios productos por precio min y precio max

async def obtener_por_precio(min_price, max_price):
    if min_price> max_price:
        raise HTTPException(status_code=400, detail= 'El precio minimo no puede ser mayor que el maximo')
    try:
        conn=await get_connection() #abrimos conexion
        async with conn.cursor(aiomysql.DictCursor) as cursor: #coloca el cursor abajo.espera a recibir la consulta
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE price BETWEEN %s AND %s',(min_price, max_price))
            data= await cursor.fetchall()
        if data:
            return data
        else:
            raise HTTPException(status_code=404 , detail='Producto no encontrado')
    except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()


#una ruta que me permita sacar un producto por su titulo. deberá devolverme listado de productos
async def obtener_por_titulo(title):
    #es buena practica el hacer 1º un print(title) para ver si nos lo devuelve y todo va bien
    try:
        conn = await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(
                'SELECT * FROM upgrade_shop.products WHERE LOWER(title) LIKE %s', (f'%{title.lower()}%',))
            data = await cursor.fetchall()
        if len(data) !=0:
            return data
        else:
            raise HTTPException(status_code=404, detail='Producto no encontrado')

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')
    finally:
        conn.close()
    

#una ruta que me permita devolver un listado de productos que no esten en stock.status:1
async def get_by_stock(status: int):
    try:
        conn = await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute('SELECT * FROM upgrade_shop.products WHERE status=%s', (status,))
            data = await cursor.fetchall()
            if len(data) != 0:
                return data
            else:
                raise HTTPException(
                    status_code=404, detail='No hay resultados')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()

#una ruta que me permita devolver un listado de productos con cantidad mayor de 10

async def get_by_quantity(quantity: str, compare: str):
    # usamos quantity como str para poder comprobar si no es un digito y o es negativo.
    if not quantity.isdigit():
        raise HTTPException(
            status_code=422, detail='Cantidad tiene que ser un numero y no puede ser negativa')
    # como estamos tratando el quantity como str lo tenemos que convertir a numero
    quantity = int(quantity)
    try:
        conn = await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            if compare == 'gt':
                query = 'SELECT * FROM upgrade_shop.products WHERE quantity>=%s'
            else:
                query = 'SELECT * FROM upgrade_shop.products WHERE quantity<=%s'
            await cursor.execute(query, (quantity,))
            data = await cursor.fetchall()
            if len(data) != 0:
                return data
            else:
                raise HTTPException(
                    status_code=404, detail='No hay resultados')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()

    
async def delete_product(id_product:int):
    product = await obtener_por_id(id_product)
    if product:
        try:
            conn = await get_connection()
            async with conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute("DELETE FROM upgrade_shop.products WHERE id=%s", (id_product, ))
                await conn.commit() #confirmo una sentencia no extraigo datos
                return {'msg':f'El producto con id {id_product} ha sido eliminado exitosamente', 'status':True, 'icon':'success'}
        except Exception as e:
            raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
        finally:
            conn.close()
    else:
        raise HTTPException(status_code=404, detail=f'Producto con id {id_product} no encontrado')
    

async def create_product(product:ProductCreate):
    try:
        conn = await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("INSERT INTO upgrade_shop.products (title, quantity, status, price) VALUES (%s, %s, %s, %s)", (
                product.title,
                product.quantity,
                product.status,
                product.price
            ))
            await conn.commit() #hay que darle al rayito. hace el commit
            nuevo_id = cursor.lastrowid #me devuelve el id
            product = await obtener_por_id(nuevo_id)
            return product
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error: {str(e)}')
    finally:
        conn.close()


async def update_product(id_product:int, product:Product):
    if id_product != product.id:
        raise HTTPException(status_code=400, detail= "los ID no coinciden")
    try:
        conn= await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("UPDATE upgrade_shop.products SET title=%s, quantity=%s, status=%s, price=%s WHERE id=%s", (
                product.title,
                product.quantity,
                product.status,
                product.price,
                product.id
                ))
            await conn.commit() #le damos al rayito
            #ya tenemos el id de producto, ahora respondemos con el producto actualizado
            product= await obtener_por_id(id_product) #porque necesitamos el id
            return{"msg": 'Producto actualizado correctamente', "item":product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()