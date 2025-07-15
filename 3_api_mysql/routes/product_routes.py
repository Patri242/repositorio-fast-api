from fastapi import APIRouter
from controllers import product_controller

router = APIRouter()


#http://localhost:8000/products/
@router.get('/', status_code=200)
async def get_all():
    return await product_controller.get_products_list()

#realizar todo el flujo para obtener un producto por id
@router.get('/id/{id_product}', status_code=200)
async def get_by_id(id_product:int):
    return await product_controller.obtener_por_id(id_product)


@router.get('/price/{min_price}/{max_price}', status_code=200)
async def get_by_price(min_price:float, max_price:float):
    return await product_controller.obtener_por_precio(min_price, max_price)

@router.get('/title/{title}', status_code=200)
async def get_by_title(title:str):
    return await product_controller.obtener_por_titulo(title)

@router.get('/stock/0', status_code=200)
async def get_by_stock():
    return await product_controller.obtener_por_stock()

@router.get('/quantity', status_code=200)
async def get_by_quantity():
    return await product_controller.obtener_por_cantidad()