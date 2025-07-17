from fastapi import HTTPException
from db.config import get_connection
from models.user_model import UserCreate, UserLogin
from core.security import hash_password, verify_password, create_token
from controllers.user_controller import obtener_usuario
import aiomysql



async def registrar_usuario(user:UserCreate):
    try:
        conn=await get_connection() #crear la conexion
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            hashed_password= hash_password(user.password)
            #en la corta era en la que habia que seguir el orden.
            await cursor.execute("INSERT INTO upgrade_shop.users(name, age, surname, email, password, rol) VALUES (%s, %s, %s, %s, %s, %s)", (
                user.name,
                user.age,
                user.surname,
                user.email,
                hashed_password,
                user.rol
            ))
            await conn.commit()
            new_id = cursor.lastrowid
            user= await obtener_usuario(new_id)
            return { 'msg': 'Usuario registrado correctamente', 'item':user}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close() 


async def login(user_login: UserLogin):
    try:
        conn=await get_connection()
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute("SELECT * FROM upgrade_shop.users WHERE email= %s", (user_login.email, ))
            user =await cursor.fetchone()

            if not user:
                raise HTTPException(status_code=404, detail='Usuario o password incorrectos')
            #verificar contraseña
            if not verify_password(user_login.password, user['password']):
                raise HTTPException(status_code=404, detail='Usuario o password incorrectos')
            #crear el token
            token_data={
                "id":user['id'],
                "rol":user['rol'] 
            }
            token = create_token(token_data)
            #aqui podemos retornar lo que queramos
            return {
                'token':token,
                'type':'bearer',
                'usuario': {
                    'id': user['id'],
                    'name':user['name'],
                    'rol':user['rol'],
                    'email':user['email']
                }
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
    finally:
        conn.close()