#necesitamos las librerias de python python-jose => criptografia, passlib => bycrypt
#pip install "python-jose[cryptography]"
#pip install "passlib[bcrypt]"
import os #me permite acceder a ficheros del sistema operativo. porque tenemos que cargar las variables de entorno
from datetime import datetime, timedelta, timezone #para la expiracion del token
#parametros opcionales
#from typing import Optional
#libreria de seguridad y encriptacion
from jose import JWTError,jwt
#para hashear contraseñas utilizamos la libreria
from passlib.context import CryptContext
#variables de entorno
from dotenv import load_dotenv


#cargar las variables de entorno
load_dotenv()

#leer las variables de entorno y almacenarlas para nuestro uso en este fichero
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

#configurar bcrypt parsa poderlo usar en est fichero. generar un contexto.
pwd_context= CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash_password(password:str):
    #hashea la contraseña usando bcrypt
    return pwd_context.hash(password)


def verify_password(plain_password:str, hashed_password:str):
    #Verifica que una contraseña en texto plano coincida con su hash
    return pwd_context.verify(plain_password, hashed_password)

#crear un token de logeo de usuario. contraseña temporal que tiene una duracion.
#un token se forma con el id del usuario, el rol, fecha de expiración{id: user.id, rol: user.rol}
#dos funciones, una para crear el token y devolverlo y otra para decodificarlo

def create_token(data:dict):
    #crear un token con la libreria jwt con los datos de usuario y expiracion
    data_copy_to_encode = data.copy() #los arrays y los diccionarios se copian con el metodo de copia.
    #calcular el tiempo de expiracion usando la variable ACCESS_TOKEN en minutos
    expire = datetime.now(tz=timezone.utc) + timedelta(minutes=ACCESS_TOKEN)

    #crear objeto {id:user.id, rol:user.rol, expire:tiempo}

    data_copy_to_encode.update({'expire': int(expire.timestamp())}) #ahora es float.milisegundos

    #codificarlo
    return jwt.encode(data_copy_to_encode, SECRET_KEY, algorithm=ALGORITHM) #dos metodos, encode y decode

#print(create_token({'id':2, 'rol':'admin'}))

#funcion para decodificaar un token´
def decode_token(token:str):
    #decodificar el token pra recibir lso datos del usuario.son id. rol. fecha de expiracion. Para ello usamos la libreria JWT
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        return None
    
