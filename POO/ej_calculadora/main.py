from Calculadora import Calculadora #asi tenemos importados todos los metodos


# instanciar el objeto calculadora, crear una calculadora en base a la clase
#casio= Calculadora() #estamos llamando al objeto. cuando genero una clase siempre hay un metodo que se ejecuta al instanciar... cuando lo ejecuto estoy ejecutando el metodo constructor
#resultado = casio.sumar(1,2,3,4,5,6,7) 
# ahora ejecuto la funcion sumar-> casio. y lo guardo en la variable resultado.
#print(resultado)

def main(): #Interfaz cli
    casio= Calculadora()
    interfaz = """ Calculadora:
    [1]. Sumar
    [2]. Restar
    [3]. Multiplicar
    [4]. Dividir
    [x]. Salir
    """

    print(interfaz)
    option= input('¿Qué operacion quieres realizar?: ')
    print(option)
    if option == '1':
        lista_numeros= [] #es el array donde queremos guardar los numeros
        cantidad = int (input('Dime cuantos numeros quieres sumar: ')) #la cantidad es un numero, que es el input de
        #el for range va hasta el numero final sin incluir el ultimo
        for i in range (0, cantidad):
            numero = int(input('Dime un numero: '))
            lista_numeros.append(numero) #metodo para añadir
        print(casio.sumar(lista_numeros))
        
    elif option == '2':
        numero1 = float(input ('Dime el primer numero: '))
        numero2 = float(input('Dime el segundo numero distinto de 0: '))
        print(casio.restar(numero1, numero2))
        
    elif option == '3':
        numero1 = float(input('deme el primer numero: '))
        numero2 = float(input('deme el primer numero: '))
        numero3 = float(input('deme el primer numero: '))
        print(casio.multiplicar(numero1,numero2,numero3))

    elif option == '4':
        numero1 = float(input ('Dime el primer numero: '))
        numero2 = float(input('Dime el segundo numero distinto de 0: '))
        print(casio.dividir(numero1, numero2))
        
    elif option == 'x':
        print('Hasta pronto!')
    else:
        print('Opcion no valida')
        main()

if __name__ == '__main__':  #que se ejecute el main al iniciar
    main()