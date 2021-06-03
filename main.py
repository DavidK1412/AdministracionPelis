# Importamos la librería OS para usar SYSTEM y poder limpiar pantalla
import os

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
total_alquilos = []
valor_total_alquilado = 0

# Función para limpiar pantalla
def limpiar_pantalla():
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    os.system(var)

#Función para mostrar las películas disponibles
def mostrar_peliculas():
    limpiar_pantalla()
    print("===================Películas disponibles=================")
    print()
    for i in range(cantidad_peliculas):
        print(f"Película #{i + 1}: Título:", arr_pelis[i].nombre, " Genero:", arr_pelis[i].genero, " Año:", arr_pelis[i].anio, " Valor:", "$", arr_pelis[i].precio)
        print("-------------------------------------------------------------------------------------------------------")
    
    print("Digite 1 Para alquilar una película")
    print("Digite 0 Para volver al menú")
    menu_tecla = int(input("Digite una opción: "))

    return menu_tecla



#Función para el desplegar el menú principal
def menu():
    opcion_menu = 0
    # Llamada a la función de limpiar pantalla
    limpiar_pantalla()

    print("-----------------------------------------------------")
    print("------- Menú Principal -------------")
    print()
    print("Digite 1 para ver todas las películas disponibles")
    print("Digite 2 para filtrar las películas disponibles")
    print("Digite 3 para alquilar una película")
    print("Digite 0 para salir")
    opcion_menu = int(input("Digite una opción: "))

    #Condición para mostrar el listado de películas
    if opcion_menu == 1:
        mostrar_peliculas()
    elif opcion_menu == 2:
        filtrar_peliculas()
    elif opcion_menu == 0:
        print("Gracias por utilizar nuestro sistema, ¡vuelva pronto!")

def filtrar_peliculas():
    opcion_submenu = 0
    # Llamada a la función de limpiar pantalla
    limpiar_pantalla()

    print("-----------------------------------------------------")
    print("------- Filtro de películas -------------")
    print()
    print("Digite 1 para ver las películas de acción")
    print("Digite 2 para ver las películas de terror")
    print("Digite 3 para ver las películas Infantiles")
    print("Ingrese 0 para volver")
    opcion_submenu = int(input("Por favor, digite una opción: "))

    if opcion_submenu == 0:
        menu()

menu()