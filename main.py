class Pelicula(): # CLASE INICIALIZADORA DE PELICULAS, NOMBRE Y GENERO SON DATOS DE TIPO STRING, AÑO ES TIPO ENTERO Y PRECIO DE TIPO FLOTANTE
    def __init__(self, nombre, genero, anio, precio):
        self.nombre = nombre
        self.genero = genero
        self.anio = anio
        self.precio = precio



pelicula1 = Pelicula("Spiderman", "SuperHeroes", 2002, 10.000) # EJEMPLO DE COMO SE PUEDE CREAR UN OBJETO

status = True
menu_tecla = ""
tecla_submenu = ""
total_alquilos = []
valor_total_alquilado = 0
arr_pelis = [pelicula1] 
##OBJETOS DE LAS PELICULAS: 5 ACCIÓN/SUPERHEROES, 5 TERROR, 5 NIÑOS/FICCION y 5 DRAMA/COMEDIA

print(arr_pelis[0].nombre) # Print para probar si se han añadido bien los objetos

def final():
    status = False
    print(total_alquilos)

def menu():
    print("Ingrese 1 para mostrar los nombres de las peliculas")
    print("Ingrese 2 para comenzar a filtrar")
    print("Ingrese 3 para alquilar")
    print("Ingrese 0 para salir")

def filtrar_peliculas():
    print("Ingrese 1 para mostrar los nombres de las peliculas")
    print("Ingrese 2 para comenzar a filtrar")
    print("Ingrese 3 para alquilar")
    print("Ingrese 0 para volver")
##while status == True:
