#como es una clase en mayus
class Calculadora: #en cuanto declare un objeto calculadora, new calculadora
    #como no voy a inicializar ninguna propiedad de la clase no necesito el metodo __init__(constructor) NO ES OBLIGATORIO.

    def sumar(self, numeros): # *numeros(split operator) no representa una lista- sería 1,2,3 x ejemplo, pero hemos dicho que vamos a usar un tipo lista. numeros representa una variable que es tipo lista
        #en javascript era ... . es una array pero en python se llama lista
        resultado = 0
        for numero in numeros: #recorremos para calcular cada numero
            resultado += numero
        return resultado
        

    def restar(self, n1, n2): #ternario. Funcion
        return n1 - n2 if n1>=n2 else n2 - n1
        """
        resultado=0
        if n1>n2:
            resultado=n2-n1 
        else:
            resultado=n1-n2
        return resultado
        """
    def multiplicar(self, *numeros):
        resultado = 1.
        for numero in numeros:
            resultado *= numero 
        return resultado

    def dividir(self, n1, n2):
        try:                    #Elemento de control de excepciones. Lo suyo en vez de un if =!... Python excepciones. Como el try catch de angular
            return n1/n2
        except ZeroDivisionError:
            print('No se puede dividir por cero')


#tenemos el plano pero no lo hemos construido aún