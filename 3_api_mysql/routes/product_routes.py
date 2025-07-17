from fastapi import APIRouter
from controllers import product_controller
from models.product_model import Product, ProductCreate

router = APIRouter()


#http://localhost:8000/products/
@router.get('/', status_code=200)
async def get_all():
    return await product_controller.get_products_list()

#realizar todo el flujo para obtener un producto por id
@router.get('/id/{id_product}', status_code=200)
async def get_by_id(id_product:int):
    return await product_controller.obtener_por_id(id_product)


@router.get('/price/{min_price}/{max_price}', status_code=200) #parametros fijos->mas aesthetic. o query params.
async def get_by_price(min_price:float, max_price:float):
    return await product_controller.obtener_por_precio(min_price, max_price)


@router.get('/title/{title}', status_code=200) #el buscador SIEMPRE se hace con query params.
async def get_by_title(title:str):
    return await product_controller.obtener_por_titulo(title)


@router.get('/filter/stock', status_code=200)
async def get_by_stock(status: int = 1):
    return await product_controller.get_by_stock(status)


@router.get('/filter/quantity/{quantity}')
async def get_by_quantity(quantity: str, compare: str = 'gt'):
    return await product_controller.get_by_quantity(quantity, compare)

#borrar producto. para no borrar la base de datos borramos por id. cambia el verbo
@router.delete('/{id_product}', status_code=200)
async def delete_product(id_product: int):
    return await product_controller.delete_product(id_product)

#crear producto.POST mandando la info del producto que queremos registrar. sin ID. la respuesta me devuelve el producto con id y sus datos completos
@router.post('/', status_code=201)
async def create_product(product: ProductCreate):
    return await product_controller.create_product(product)

#actuañizacion de un producto : PUT/PATCH. patch solo actualiza x campo, uno, varios.., put el objeto entero, con todos los campos. Actualizamos la informacion de la BBDD. usa ID.respuesta será min. el producto actualizado.
@router.put('/{id_product}', status_code=200)
async def update_product(id_product:int, product:Product): #el orden importa
    return await product_controller.update_product(id_product,product)
        
