#4º importar el user_model
#from models import user_model PEERO hay una forma de importar solo las funciones:
from models.user_model import cargar_todos_usuarios, cargar_usuario_por_id, añadir_usuario, User, delete_usuario, actualizar_un_usuario, buscar_por_edad, buscar_por_email_nombre

#2º crear el user_controller
def obtener_usuarios():
    #return [{'id':1, 'name':'juan', 'age':42}]
    return cargar_todos_usuarios()


def obtener_usuario_por_id(id:int):
    return cargar_usuario_por_id(id)


def insertar_usuario(usuario: User):
    return añadir_usuario(usuario)

def actualizar_usuario(id:int, usuario: User):
    return actualizar_un_usuario(id, usuario)

def borrar_usuario(id:str):
    return delete_usuario(id)

def filter_by_age(agemin:int,agemax:int):
    return buscar_por_edad(agemin,agemax)

def filter_by_text(busqueda:str):
    return buscar_por_email_nombre(busqueda)

#el controlador se encarga de llamar a las ases de datos