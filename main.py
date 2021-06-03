# Importamos la librería OS para usar SYSTEM y poder limpiar pantalla
import os
import copy # Libreria para copiar

class Pelicula:  # CLASE INICIALIZADORA DE PELICULAS, NOMBRE Y GENERO SON DATOS DE TIPO STRING, AÑO ES TIPO ENTERO Y PRECIO DE TIPO FLOTANTE
    def __init__(self, nombre, genero, anio, precio):
        self.nombre = nombre
        self.genero = genero
        self.anio = anio
        self.precio = precio

#Colocamos en una variable una cantidad predefinida de películas
cantidad_peliculas_vista_user = 20 # Será para mostrarle al usuario, podemos usar el método len() para obtener los indices de la lista arr_pelis

# Añadimos las películas
pelicula1 = Pelicula("Spiderman", "Superheroes", 2002, 10000)  # Eliminados los puntos al final de cada titulo/genero, facilitará el manejo de los Strings
pelicula2 = Pelicula("Venom: Let There Be Carnage", "Superheroes", 2021, 20000)
pelicula3 = Pelicula("Rapidos y Furiosos 4", "Acción", 2009, 12000)
pelicula4 = Pelicula("La caida del Halcón negro", "Acción", 2001, 13000)
pelicula5 = Pelicula("Sherlock Holmes", "Aventura", 2009, 15000)
pelicula6 = Pelicula("Divergente", "Acción", 2014, 14000)
pelicula7 = Pelicula("Wonder Woman", "Acción", 2020, 18000)
pelicual8 = Pelicula("Coco", "Infantil", 2017, 15000)
pelicual9 = Pelicula("Soul", "Infantil", 2020, 16000)
pelicula10 = Pelicula("El libro de la vida", "Infantil", 2014, 12000)
pelicula11 = Pelicula("El Conjuro 3: el diablo me obligó a hacerlo", "Terror", 2021, 20000)
pelicula12 = Pelicula("REC", "Terror", 2007, 11000)
pelicula13 = Pelicula("¿Y dónde están las rubias?", "Comedia", 2004, 10000)
pelicula14 = Pelicula("Supercool", "Comedia", 2007, 10000)
pelicula15 = Pelicula("No se metan con Zohan", "Comedia", 2008, 12000)
pelicula16 = Pelicula("Indiana Jones y la última cruzada", "Aventura", 1989, 10000)
pelicula17 = Pelicula("Jumanji: En la selva", "Aventura", 2017, 16000)
pelicula18 = Pelicula("El gran Gatsby", "Drama", 2013, 13000)
pelicula19 = Pelicula("Perfume: La historia de un asesino","Drama", 2006, 11000)
pelicula20 = Pelicula("El tigre blanco", "Drama", 2021, 20000)


#Arreglo para guardar las películas
##OBJETOS DE LA PELICULA 5 ACCIÓN/SUPERHEROES, 5 TERROR, 5 NIÑOS/FICCION y 5 DRAMA/COMEDIA
arr_pelis = [pelicula1, pelicula2, pelicula3,pelicula4,pelicula5,pelicula6,pelicula7,pelicual8,pelicual9,pelicula10,pelicula11,pelicula12,pelicula13,pelicula14,pelicula15,pelicula16,pelicula17, pelicula18,pelicula19,pelicula20]

status = True
total_alquilos = []
valor_total_alquilado = 0
input_string = ""
arr_filtro = []
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
    for i in range(cantidad_peliculas_vista_user):
        print(f"Película #{i + 1}: Título:", arr_pelis[i].nombre, " Genero:", arr_pelis[i].genero, " Año:", arr_pelis[i].anio, " Valor:", "$", arr_pelis[i].precio)
        print("-------------------------------------------------------------------------------------------------------")
    
    print("Digite 1 Para alquilar una película")
    print("Digite 0 Para volver al menú")
    menu_tecla = int(input("Digite una opción: "))
'''    if menu_tecla == 1:
        alquilar()'''



#Función para el desplegar el menú principal
def menu():
    opcion_menu = 0
    # Llamada a la función de limpiar pantalla
    limpiar_pantalla()

    print("-----------------------------------------------------")
    print("------- Menú Principal -------------\n")
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
    print("------- Filtro de películas ------------- \n")
    print("Digite 1 para ver las peliculas según su genero")
    print("Digite 2 para ver las películas en un rango de precio")
    print("Digite 3 para ver las películas por año")
    print("Digite 4 para ver las peliculas por nombre")
    print("Ingrese 0 para volver")
    opcion_submenu = int(input("Por favor, digite una opción: "))

    if opcion_submenu == 0:
        menu()
    elif opcion_submenu == 1:
        input_string = input("Ingrese el genero que busca en nuestro catalogo: ")
        fil_gen(input_string)
    elif opcion_submenu == 2:
        opcion_submenu = input("Ingrese el precio máximo de alquiler (sin .): ")
        opcion_submenu = int(opcion_submenu)
        fil_pre(opcion_submenu)
    elif opcion_submenu == 3:
        opcion_submenu = input("Ingrese el año que desea consultar las peliculas: ")
        opcion_submenu = int(opcion_submenu)
        fil_anio(opcion_submenu)
    elif opcion_submenu == 4:
        opcion_submenu = input("Ingrese el nombre de la pelicula que busca (o una parte): ")
        fil_nombre(opcion_submenu)

def fil_gen(inp):
    arr_filtro = []
    inp = inp.lower() #Convertimos cualquier cadena en minusculas
    inp = inp.capitalize() #Hacemos que se cambie la primera letra en mayusculas

    for i in range(len(arr_pelis)):
        if (arr_pelis[i].genero == inp):
            arr_filtro.append(arr_pelis[i].nombre)
    else:
        print("Tenemos ", (len(arr_filtro)), " peliculas de ", inp.lower(), " disponibles :", arr_filtro)
    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()

def fil_pre(p_max):
    arr_filtro = []
    text_fil_pre = ""
    for i in range(len(arr_pelis)):
        if (arr_pelis[i].precio <= p_max):
            text_fil_pre = arr_pelis[i].nombre + " con el precio de: $" + str(arr_pelis[i].precio)
            arr_filtro.append(text_fil_pre)
    else:
        print("Tenemos ", (len(arr_filtro)), " pelicula(s) de menor o igual precio de ", p_max, " disponibles :", arr_filtro)
    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()

def fil_anio(anio):
    text_fil_an = ""
    arr_filtro = []
    for i in range(len(arr_pelis)):
        if (arr_pelis[i].anio == anio):
            text_fil_an = arr_pelis[i].nombre + " del año: " + str(arr_pelis[i].anio)
            arr_filtro.append(text_fil_an)
    else: print("Tenemos ", len(arr_filtro), "pelicula(s) del año: ", anio, " : ", arr_filtro)
    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()
def fil_nombre(nom):
    arr_filtro = []
    copy_arr = copy.deepcopy(arr_pelis)
    nom = nom.lower()
    for i in range(len(copy_arr)):
        copy_arr[i].nombre = copy_arr[i].nombre.lower()
        if (copy_arr[i].nombre.find(nom) >= 0 or copy_arr[i].nombre == nom):
            arr_filtro.append(arr_pelis[i].nombre)
    else:
        print("Coinciden con la busqueda de \'", nom, "\' : ", arr_filtro)
    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()
menu()