from fastapi import APIRouter
from controllers import product_controller

router = APIRouter()


#http://localhost:8000/products/
@router.get('/', status_code=200)
async def get_all():
    return await product_controller.get_products_list()

#realizar todo el flujo para obtener un producto por id
@router.get('/{id_product}', status_code=200)
async def get_by_id(id_product):
    return await product_controller.obtener_por_id(id_product)
