from fastapi import APIRouter, Depends
from controllers import user_controller
from models.user_model import User, UserCreate
from core.dependencies import is_admin_or_owner

router = APIRouter()

@router.get('/', status_code=200)
async def get_all():
    return await user_controller.lista_usuarios()

@router.get('/{id_user}', status_code=200)
async def get_user_id(id_user:int):
    return await user_controller.obtener_usuario(id_user)

@router.put('/{id_user}', status_code=200)
async def update_user(id_user:int, user:User, user1= Depends(is_admin_or_owner)):
    return await user_controller.actualizar_usuario(id_user,user)


@router.delete('/{id_user}', status_code=200)
async def delete_user(id_user:int, user= Depends(is_admin_or_owner)):
    return await user_controller.borrar_usuario(id_user)



