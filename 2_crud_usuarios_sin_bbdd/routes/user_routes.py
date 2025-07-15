from fastapi import APIRouter #2º la libreria de fastapi que nos permite usar las rutas. 
from controllers import user_controller
from models.user_model import User
#en este fichero ya nos encontramos en la ruta /users, todas las rutas de aqui dentro tendran esa base

#Fichero pensado para rutas

router= APIRouter()

@router.get('/', status_code=200)#obtener todos los usuarios
def get_users():
    return user_controller.obtener_usuarios()

@router.get('/{id}', status_code=200)#obtener un usuario por id
def get_users_by_id(id:str):
    return user_controller.obtener_usuario_por_id(int(id))

@router.post('/', status_code=201) #instert un usuario
def insert_user(usuario: User):
    return user_controller.insertar_usuario(usuario)

@router.put('/{id}', status_code=200)
def update_user(id:int, usuario: User):
    return user_controller.actualizar_usuario(id, usuario) #{'msg': f'actualizar un usuario con id {id}'} template f

#quiero que implementeis en 5 minutos el borrado del un usuario del array, debereis devolver la lista de usuarios sin el usuario que quiero borrar.

@router.delete('/{id}', status_code=200)
def delete_user(id:str):
    return user_controller.borrar_usuario(int(id))
    #return {'msg': f'Borrar un usuario'}

#query params. Parámetros que no tienen una ruta fija. Me permiten hace busquedas por parametros mas versatiles. se usa principalmente para filtros
#ruta con filtros por edad: http://localhost:8000/users/filter/age?agemin=12&agemax=24
@router.get('/filter/age', status_code=200)
def get_user_by_age(agemin: int,agemax: int):
    #print(agemin,agemax)
    return user_controller.filter_by_age(agemin,agemax)

#http://localhost:8000/users/filter/search?busqueda=juanantonio
@router.get('/filter/search', status_code=200)
def get_user_by_search(busqueda:str):
    #return(busqueda)
    return user_controller.filter_by_text(busqueda)