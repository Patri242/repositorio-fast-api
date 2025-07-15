from pydantic import BaseModel #3º creamos user_model pydantic es una clase
from fastapi import HTTPException


class User (BaseModel): #modelos SIEMPRE en singular. tipo clase
    id: int
    name:str
    age:int
    email:str

usuarios= [ #tipo diccionario
    {"id": 1, "name": "Alice", "age": 25, "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "age": 30, "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "age": 22, "email": "charlie@example.com"},
    {"id": 4, "name": "Diana", "age": 28, "email": "diana@example.com"},
    {"id": 5, "name": "Eve", "age": 35, "email": "eve@example.com"},
    {"id": 6, "name": "Frank", "age": 40, "email": "frank@example.com"},
    {"id": 7, "name": "Grace", "age": 27, "email": "grace@example.com"},
    {"id": 8, "name": "Hank", "age": 32, "email": "hank@example.com"},
    {"id": 9, "name": "Ivy", "age": 29, "email": "ivy@example.com"},
    {"id": 10, "name": "Jack", "age": 24, "email": "jack@example.com"},
]

def cargar_todos_usuarios(): #cuando tengamos bases de datos no tiene sentido esta funcion
    return usuarios


def cargar_usuario_por_id(id:int):
    for usuario in usuarios:
        if usuario['id'] == id:
            return usuario
    raise HTTPException(status_code=404, detail='Usuario no encontrado')
    #else:
        #return {'message': f"el usuario con id {id} no existe"}

def buscar_usuario_email(email: str):
    for usuario in usuarios:
        if usuario['email'] == email:
            return True
    return False


def añadir_usuario(usuario: User): #que no se pueda hacer append si no existe en la base de datos
    email_existe= buscar_usuario_email(usuario.email) #un objeto de tipo clase
    if not email_existe:
        #model_dump() e suna funcion que convierte un usuario de tipo User en un diccionario para hacer append en el array
        usuarios.append(usuario.model_dump()) #pasar 'usuario' a diccionario. 
        return usuarios
    else:
        #return{'msg': 'Usuario duplicado'}
        raise HTTPException(status_code=400, detail='Usuario duplicado')
    
def buscar_usuario_id(id:int):
    for usuario in usuarios:
        if usuario['id']== id:
            return usuarios
        else:
            raise HTTPException(status_code=400, detail='Usuario duplicado')
            #return {'msg': 'Usuario duplicado'}
    

def delete_usuario(id:int):
        usuario_borrar = cargar_usuario_por_id(id)

        if usuario_borrar and usuario_borrar['id']:
            usuarios.remove(usuario_borrar)
            return usuarios
        else:
            raise HTTPException(status_code=400, detail='Usuario no existe')
            #return{'msg': 'Usuario no existe'}


def actualizar_un_usuario(id:int, usuario: User):
        if id != usuario.id:
            raise HTTPException(status_code=400, detail='Usuario no existe')
            #return{'msg':'El ID del cuerpo y el ID de la url no coinciden'}
        for cont,user in enumerate(usuarios):
            if user['id'] ==id: #comprobación del usuario, recorro y voy comprobando id a id si coinciden
                usuarios[cont] = usuario.model_dump() #es de tipo diccionario
                print(usuarios)
                return usuarios[cont]
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
        #return {'msg' 'Usuario no encontrado'}

def buscar_por_edad(agemin:int,agemax:int):
    if agemin > agemax:
        raise HTTPException(status_code=400, detail='La edad mínima no puede ser mayor que la máxima')
    #el raise es como un return para las excepciones
    #son varios asi q necesito un array vaciopara la busqueda
    usuarios_busqueda=[]
    for user in usuarios:
        if user['age'] >= agemin and user['age'] <= agemax:
            usuarios_busqueda.append(user)
    return usuarios_busqueda
#si tengo un array vacio no es una excepcion, simplemente no hay 

def buscar_por_email_nombre(busqueda:str):
    if busqueda == "":
        raise HTTPException(status_code=400, detail='El campo de búsqueda no puede ser vacio')
    #si el campo de busqeda no tiene nada, en cambio si el array es vacio porque no existe lo puesto, no tenemos nada, eso se podia poner con if = 0? o en el front.
    return(user for user in usuarios if busqueda.lower() in user['name'].lower() or busqueda.lower() in user['email'].lower()) # tengo que buscarlo en lowercase

    if len (usuarios_busqueda) == 0:
        return ('no se encontraron usuarios con esos criterios')
    return usuarios_busqueda

    



