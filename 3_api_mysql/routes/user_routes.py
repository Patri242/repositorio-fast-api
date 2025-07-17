from fastapi import APIRouter
from controllers import user_controller
from models.user_model import User, UserCreate

router = APIRouter()

@router.get('/', status_code=200)
async def get_all():
    return await user_controller.lista_usuarios()

@router.get('/{id_user}', status_code=200)
async def get_user_id(id_user:int):
    return await user_controller.obtener_usuario(id_user)

@router.put('/{id_user}', status_code=200)
async def update_user(id_user:int, user:User):
    return await user_controller.actualizar_usuario(id_user,user)

@router.post('/', status_code=201)
async def register_user(user:UserCreate):
    return await user_controller.registrar_usuario(user)

@router.delete('/{id_user}', status_code=200)
async def delete_user(id_user:int):
    return await user_controller.borrar_usuario(id_user)

