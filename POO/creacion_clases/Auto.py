""" se ponen los nombres de las clases en Mayus """
    #JAVASCRIPT propiedades-atributos. aqui variables para almacenar datos. y en vez de {} usamos :
class Auto: #inicializamos las propiedades
    color: str= "" #int, float, str, bool
    precio:float=0 
    combustible:str = ""
    estado: bool=True
    matricula: str= ""
    modelo:str=""
    velocidad:int=0

    #metodos-funciones-acciones que puede realizar mi objeto
    #funcion constructor no es obligatoria pero se produce siempre. se asegura de que la clase está creada. Me sirve para inicializar datos. el metodo constructor en python es __init__(). la funcion ngOnInit se asegura de que el html y el css...etc estén creados
    #las funciones se declaran con def
    def __init__(self,color,price,model,type_gas): #el objetivo de la funcion constructor es inicializar 'coche'. self representa el this.color...
        self.color = color #asigno la propiedad color
        self.precio = price #self.la funcion = la propiedad
        self.combustible = type_gas
        self.modelo=model

    def matricular(self, numero_matricula): #funcion matricular
      self.matricula = numero_matricula

    def acelera(self, velocity):
      self.velocidad += velocity
         
      """   pass """

#sería new Auto en javascript
ferrari = Auto ('rojo',100000,'f380', 'gasolina') #la indentacion. Ferrari es un objeto auto.
fiat= Auto('vino', 1500, 'topolino',)  

#falta aqui----