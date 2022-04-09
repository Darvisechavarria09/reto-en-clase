from clases.ciclista import Ciclista

opcion=1
listaCiclistas=[]
while(opcion!=0):
    print()
    print()
    print('Digite 1 para ingresar los Datos del ciclista')
    print('Digite 2 para mostrar el cilcista con el mejor tiempo')
    print()
    print()
    opcion =int(input("Digite una opcion: "));
    if(opcion==1):
        longitud=int(input("Digite la cantidad de ciclistas que desea ingresar: "))
        for i in range(longitud):
            ciclista=Ciclista()
            ciclista.nombre=input("Digite el Nombre del ciclista: ")
            ciclista.edad=int(input("Digite la Edad del ciclista: "))
            ciclista.pais=input("Digite el Pais del ciclista: ")
            ciclista.tiempo=int(input("Digite el Tiempo del ciclista en la crono: "))
            listaCiclistas.append(ciclista)
    elif(opcion==2):
        tiempoMaximo=None
        if(tiempoMaximo is None or ciclista.tiempo > tiempoMaximo):
            tiempoMaximo = ciclista.tiempo
            print('el Ciclista: ', ciclista.nombre, ' tiene el mejor tiempo que es de:', tiempoMaximo, 'Minutos')
        opcion=0
        
