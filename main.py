class Pelicula():  # CLASE INICIALIZADORA DE PELICULAS, NOMBRE Y GENERO SON DATOS DE TIPO STRING, AÑO ES TIPO ENTERO Y PRECIO DE TIPO FLOTANTE
    def __init__(self, nombre, genero, anio, precio):
        self.nombre = nombre
        self.genero = genero
        self.anio = anio
        self.precio = precio


pelicula1 = Pelicula("Spiderman", "SuperHeroes", 2002, 10.000)  # EJEMPLO DE COMO SE PUEDE CREAR UN OBJETO
pelicula2 = Pelicula("Venom: Let There Be Carnage", "SuperHeroes", 2021, 20.000)
pelicula3 = Pelicula("Rapidos y Furiosos 4", "Acción", 2009, 12.000)
pelicula4 = Pelicula("")
status = True
menu_tecla = ""
tecla_submenu = ""
total_alquilos = []
valor_total_alquilado = 0
arr_pelis = [pelicula1,
             pelicula2]  ##OBJETOS DE LA PELICULA 5 ACCIÓN/SUPERHEROES, 5 TERROR, 5 NIÑOS/FICCION y 5 DRAMA/COMEDIA

print(arr_pelis[0].nombre)


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
