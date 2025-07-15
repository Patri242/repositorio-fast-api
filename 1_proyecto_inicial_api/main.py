#importamos la libreria de fastapi
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI() #nuestro servidor

#quiero generar una ruta por GET para que me devuelva una respuesta.
#yo tengo una ruta y un verbo y me tiene que responder algo
#endpoint estatico

#decorador. Es una funcion

@app.get('/')
def root():
    return {"mensaje":
             "Hola mundo desde FastAPI"}

#crear una ruta "/mi_nombre" que me devuelva un objeto alumno con vuestro nombre

@app.get('/mi_nombre') #get es la unica peticion que no necesita postman...
#def root():  Si hacemos esto estamos perdiendo el metodo de arriba
def get_nombre():
    return {"alumno": "Maria Patricia"} #diccionario. objeto clave valor. array elemento. posicion



products = [ #creamos una lista
    {'id':1, 'name': 'Leche', 'price':12},
    {'id':2, 'name': 'Carne', 'price':22},
    {'id':3, 'name': 'Huevos', 'price':12},
    {'id':4, 'name': 'Pan', 'price':32},
    {'id':5, 'name': 'Fruta', 'price':22},
    {'id':6, 'name': 'Pescado', 'price':12},
] 

#quiero crear un endpoint estatico que me permita devolver la lista de productos /productos

@app.get('/productos')

def get_productos():
    return {'total': len(products), 'results': products}

#creamos un endpoint dinamico que me permita devolver un producto concreto

@app.get('/productos/{id}')
def get_products_by_id(id: str):
    id_producto = int(id)
    for product in products:
        if product['id'] == id_producto:
            return product
    else:
        return {'message': f"el producto con id {id_producto} no existe"}
    
#quiero un endpoint que me permita filtrar productos por precio minimo y maximo /price/22/24

@app.get('/price/{price_min}/{price_max}')
def get_products_by_price(price_min:str, price_max: str): #tienen que ser str
    result=[]
    for product in products:
        if product['price']>= float(price_min) and product['price'] <= float(price_max):
            result.append(product)
    if len(result) != 0:
        return result
    else:
        return 'No hay productos con esos precios'


#einsercion de un producto creando un modelo product. Usamos una libreria llamada pydantic

class Product(BaseModel):
    id:int
    name:str
    price:float


@app.post('/productos')
def crear_producto(producto: Product): #llama a una funcion. producto es tipo Product
    #insertar el producto en el array
    products.append(producto)
    return (products)
    # return{'msg': f'Producto {producto.name} registrado correctamente'}  
    #necesitamos un servicio, usamos postman/loqsea



#borrar un producto del array de productos
@app.delete('/productos/{id}')
def borrar_producto(id: str): 
    for product in products:
        if product['id'] == int(id):
            products.remove(product)
            return {'msg':'Producto borrado correctamente', 'result': products}
    return {'msg':'producto no existe'}
    

