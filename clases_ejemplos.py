class Persona:
    def __init__(self,dni,direccion,nacionalidad):
        dni = ""
        direccion = ""
        nacionalidad = ""

    def datos_personales(self):
        print(f"dni: {self.dni},dieccion: {self.direccion}, nacionalidad: {self.nacionalidad}")

class Heroe:( Persona ) # Heroe hereda los atributos y metodos de clase persona,Persona es la clase Padre de Heroe, Heroe es la clase hija de persona
    #varibles o atributos de la clase Heroe
   
    #funcion especial o consultor
    #se ejecuta de manera automatica al crear un objeto de la clase

    def __init__(self,name,power,nickname):
        self.nombre = name
        self.poder = power
        self.apodo = nickname
    def saludar(self):
        print(self.nombre)

    def mostrar_datos(self):
        print(f"Nombre:{self.nombre}, poder: {self.poder}, apodo: {self.apodo}")
        

#invocación de clase
#spyderman es un objeto de la clase Heroe, es una instancia de la clase Heroe

spyderman = Heroe("Peter Parker","Super fuerza","Hombre araña")
spyderman.mostrar_datos()

#print (spyderman.nombre)
#print (spyderman.apodo)
#print (spyderman.poder)


Iroman = Heroe("Tony stark","Millonario","Hombre de acero")
Iroman.mostrar_datos()

#print (Iroman.apodo)
#print (Iroman.nombre)
#print (Iroman.poder) #la funcion mostrar_datos, esto substituye todos los prints


