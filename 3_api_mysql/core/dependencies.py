from fastapi import HTTPException, Depends, Path #Middleware, hace de portero
from fastapi.security import OAuth2PasswordBearer
from db.config import get_connection
from core.security import decode_token
from controllers.user_controller import obtener_usuario

async def get_current_user(token:str):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Token inválido')
    
    user_id = payload.get('id')
    if not user_id:
        raise HTTPException(status_code=404, detail='Usuario no existe')
    #obtener los datos del usuario logeado
    user=await obtener_usuario(user_id)
    return user
