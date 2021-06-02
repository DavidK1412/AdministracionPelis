class Pelicula:  # CLASE INICIALIZADORA DE PELICULAS, NOMBRE Y GENERO SON DATOS DE TIPO STRING, AÑO ES TIPO ENTERO Y PRECIO DE TIPO FLOTANTE
    def __init__(self, nombre, genero, anio, precio):
        self.nombre = nombre
        self.genero = genero
        self.anio = anio
        self.precio = precio

#Colocamos en una variable una cantidad predefinida de películas
cantidad_peliculas = 11

# Añadimos las películas
pelicula1 = Pelicula("Spiderman.", "SuperHeroes.", 2002, 10.000)  # EJEMPLO DE COMO SE PUEDE CREAR UN OBJETO
pelicula2 = Pelicula("Venom: Let There Be Carnage.", "SuperHeroes.", 2021, 20.000)
pelicula3 = Pelicula("Rapidos y Furiosos 4.", "Acción.", 2009, 12.000)
pelicula4 = Pelicula("La caida del Halcón negro.", "Acción.", 2001, 13.000)
pelicula5 = Pelicula("Sherlock Holmes.", "Aventura.", 2009, 15.000)
pelicula6 = Pelicula("Divergente.", "Acción.", 2014, 14.000)
pelicula7 = Pelicula("Wonder Woman.", "Acción.", 2020, 18.000)
pelicual8 = Pelicula("Coco.", "Infantil.", 2017, 15.000)
pelicual9 = Pelicula("Soul.", "Infantil.", 2020, 16.000)
pelicula10 = Pelicula("El libro de la vida.", "Infantil.", 2014, 12.000)
pelicula11 = Pelicula("El Conjuro 3: el diablo me obligó a hacerlo. ", "Terror.", 2021, 20.000)


#Arreglo para guardar las películas
##OBJETOS DE LA PELICULA 5 ACCIÓN/SUPERHEROES, 5 TERROR, 5 NIÑOS/FICCION y 5 DRAMA/COMEDIA
arr_pelis = [pelicula1,
             pelicula2,
             pelicula3,
             pelicula4,
             pelicula5,
             pelicula6,
             pelicula7,
             pelicual8,
             pelicual9,
             pelicula10,
             pelicula11]

status = True
opcion_menu = 0
tecla_submenu = ""
total_alquilos = []
valor_total_alquilado = 0

#Función para mostrar las películas disponibles
def mostrar_peliculas():
    print()
    for i in range(cantidad_peliculas):
        print(f"Película #{i + 1}: Título:", arr_pelis[i].nombre, " Genero:", arr_pelis[i].genero, " Año:", arr_pelis[i].anio, " Valor:", "$", arr_pelis[i].precio)
        print("-------------------------------------------------------------------------------------------------------")

'''def final():
    status = False
    print(total_alquilos)'''

#Función para el desplegar el menú principal
def menu():
    print("------- Menú Principal -------------")
    print()
    print("Digite 1 para conocer las películas disponibles")
    print("Ingrese 2 para comenzar a filtrar")
    print("Ingrese 3 para alquilar")
    print("Ingrese 0 para salir")
    menu_tecla = int(input("Digite una opción: "))

    #Condición para mostrar el listado de películas
    if menu_tecla == 1:
        mostrar_peliculas()



'''def filtrar_peliculas():
    print("Ingrese 1 para mostrar los nombres de las peliculas")
    print("Ingrese 2 para comenzar a filtrar")
    print("Ingrese 3 para alquilar")
    print("Ingrese 0 para volver")
##while status == True:'''
menu()