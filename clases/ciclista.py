class Ciclista:

    #CONSTRUCTOR
    def __init__(self):
        #ATRIBUTOS
        self.__nombre=None
        self.__edad=None
        self.__pais=None
        self.__tiempo=None
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @property
    def pais(self):
        return self.__pais
    
    @property
    def tiempo(self):
        return self.__tiempo

    #Setters
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    @edad.setter
    def edad(self,edad):
        if(edad<0):
            print('no acepto edades negativas')
            self.__edad=0
        else:
            self.__edad=edad
    
    @pais.setter
    def pais(self,pais):
        self.__pais=pais
    
    @tiempo.setter
    def tiempo(self,tiempo):
        if(tiempo<0):
            print('no acepto tiempos menores a 0')
            self.__tiempo=None
        else:
            self.__tiempo=tiempo