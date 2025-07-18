#archivo de dependencias me permite bloquear el acceso a ciertas rutas en función de ciertas características, si es usuario valido o el tipo de rol que tiene. 1º generamos api, luego autentificacion
from fastapi import HTTPException, Depends, Path
from fastapi.security import OAuth2PasswordBearer
from db.config import get_connection
from controllers.user_controller import obtener_usuario
import aiomysql
from core.security import decode_token

#A las dependencias hay que indicarles donde y cuando se genera el token. 
oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login") #donde se genera el token


async def get_current_user(token:str = Depends(oauth2)):
    #decodificar el token
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail='Token invalido')
    user_id = payload.get('id')
    if not user_id:
        raise HTTPException(status_code=404, detail='Este usuario no existe')
#obtener los datos del usuario logeado
    user = await obtener_usuario(user_id)
    return user

#verificar si soy rol administrador o el propio usuario, esta dependencia nos servirá para aplicar  EL CRUD de usuarios
async def is_admin_or_owner(user=Depends(get_current_user), id_user:int = Path(...)):
    #Verificar si el usuario autenticado es admin o es el dueño del recurso. Si no se cumple, lanzo una excepcion.
    #si el usuario es admin, permitir
    if user.get('rol') == 'admin':
        return user #el return me saca de la funcion. secuencia de salida.
    #si el usuario es el dueño del recurso
    if user['id'] == id_user: #esto y el if de arriba son lo mismo
        return user
    #si no es admin ni es dueño del recurso, deniego el acceso
    raise HTTPException(status_code=403, detail='No tienes permisos para realizar esta acción')
    
