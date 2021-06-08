# Importamos la librería OS para usar SYSTEM y poder limpiar pantalla
from io import open_code
import os
import copy # Libreria para copiar
import random
import time

class Pelicula:  # CLASE INICIALIZADORA DE PELICULAS, NOMBRE Y GENERO SON DATOS DE TIPO STRING, AÑO ES TIPO ENTERO Y PRECIO DE TIPO FLOTANTE
    def __init__(self, id, nombre, genero, anio, precio):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.anio = anio
        self.precio = precio

#Colocamos en una variable una cantidad predefinida de películas
cantidad_peliculas_vista_user = 20 # Será para mostrarle al usuario, podemos usar el método len() para obtener los indices de la lista arr_pelis

# Añadimos las películas
pelicula1 = Pelicula(1, "Spiderman", "Superheroes", 2002, 10000)  # Eliminados los puntos al final de cada titulo/genero, facilitará el manejo de los Strings
pelicula2 = Pelicula(2, "Venom: Let There Be Carnage", "Superheroes", 2021, 20000)
pelicula3 = Pelicula(3, "Rapidos y Furiosos 4", "Acción", 2009, 12000)
pelicula4 = Pelicula(4, "La caida del Halcón negro", "Acción", 2001, 13000)
pelicula5 = Pelicula(5, "Sherlock Holmes", "Aventura", 2009, 15000)
pelicula6 = Pelicula(6, "Divergente", "Acción", 2014, 14000)
pelicula7 = Pelicula(7, "Wonder Woman", "Acción", 2020, 18000)
pelicual8 = Pelicula(8, "Coco", "Infantil", 2017, 15000)
pelicual9 = Pelicula(9, "Soul", "Infantil", 2020, 16000)
pelicula10 = Pelicula(10, "El libro de la vida", "Infantil",  2014, 12000)
pelicula11 = Pelicula(11, "El Conjuro 3: el diablo me obligó a hacerlo", "Terror", 2021, 20000)
pelicula12 = Pelicula(12, "REC", "Terror", 2007, 11000)
pelicula13 = Pelicula(13, "¿Y dónde están las rubias?", "Comedia", 2004, 10000)
pelicula14 = Pelicula(14, "Supercool", "Comedia", 2007, 10000)
pelicula15 = Pelicula(15, "No se metan con Zohan", "Comedia", 2008, 12000)
pelicula16 = Pelicula(16, "Indiana Jones y la última cruzada", "Aventura", 1989, 10000)
pelicula17 = Pelicula(17, "Jumanji: En la selva", "Aventura", 2017, 16000)
pelicula18 = Pelicula(18, "El gran Gatsby", "Drama", 2013, 13000)
pelicula19 = Pelicula(19, "Perfume: La historia de un asesino","Drama", 2006, 11000)
pelicula20 = Pelicula(20, "El tigre blanco", "Drama", 2021, 20000)


#Arreglo para guardar las películas
##OBJETOS DE LA PELICULA 5 ACCIÓN/SUPERHEROES, 5 TERROR, 5 NIÑOS/FICCION y 5 DRAMA/COMEDIA
arr_pelis = [pelicula1, pelicula2, pelicula3,pelicula4,pelicula5,pelicula6,pelicula7,pelicual8,pelicual9,pelicula10,pelicula11,pelicula12,pelicula13,pelicula14,pelicula15,pelicula16,pelicula17, pelicula18,pelicula19,pelicula20]

status = True
input_string = ""
arr_filtro = []

#===================== INICIO LIMPIAR PANTALLA =================================
def limpiar_pantalla():
    if os.name == "posix":
        var = "clear"
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        var = "cls"
    os.system(var)
#==================== FIN LIMPIAR PANTALLA =====================================

#==================== INICIO PELÍCULA RECOMENDADA ==============================
#Se guarda en una variable una palícula aleatoria
random_peli = random.choice(arr_pelis)
def pelicula_aleatoria():
        print("{:^93}".format("Película Recomendada"))
        print("{}".format("-"*93))
        print("{0:<3} {1:<50} {2:<12} {3:^12} {4:>12}".format("Id","Título", "Género", "Año", "Precio"))
        print("{}".format("-"*93))
        print("{0:<3} {1:<50} {2:<12} {3:^12} {4:>11}".format(random_peli.id,random_peli.nombre, random_peli.genero, random_peli.anio, f"$ {random_peli.precio}"))
        print()
#====================== FIN PELÍCULA RECOMENDADA ===============================

#================== INICIO ALQUILAR PELÍCULA ===================================

#--------------------- INICIO FUNCIÓN SELECCIONAR PELÍCULA ---------------------
peliculas_alquiladas = []
def alquilar_pelicula():
    limpiar_pantalla()
    print("{:^93}".format("Bienvenido al alquiler de películas"))
    print("{}".format("-"*93))
    print()
    opcion_menu = int(input("¿cuántas películas desea alquilar?: "))
    print("{}".format("-"*93))
    print()
    peliculas_disponibles()
    evitar_duplicado = 0
    i = 1
    while i <=opcion_menu :
        seleccionar_peli = int(input("Digite el ID de la película #{} deseada: ".format(i)))

        #Ciclo para evitar que ingresen la misma película dos veces
        while not evitar_duplicado != seleccionar_peli:
            print()
            print("La película seleccionada ya se encuentra agregada")
            print()
            seleccionar_peli = int(input("Digite el ID de la película #{} deseada: ".format(i)))
            
        for j in range(len(arr_pelis)):
            indice_arreglo_peli = arr_pelis.index(arr_pelis[j])
            if indice_arreglo_peli + 1 == seleccionar_peli:
                print("{}".format("-"*93))
                print("{:<3} Se agregó '{}' correctamente".format("", arr_pelis[j].nombre))
                print("{}".format("-"*93))
                #Agregamos las películas seleccionadas a la lista
                peliculas_alquiladas.append(arr_pelis[j])
        evitar_duplicado = seleccionar_peli
        
        i += 1
    #Función para que la pantalla se mantenga un tiempo antes de cambiar a la factura
    time.sleep(2)
    mostrar_total_alquiler()
#------------------ FIN FUNCIÓN SELECCIONAR PELÍCULA ---------------------------

#------------------ INICIO FUNCIÓN MOSTRAR FACTURA -----------------------------
def mostrar_total_alquiler():
    limpiar_pantalla()
    sumar_precios = 0
    print("{:^93}".format("Factura"))
    print("{}".format(""*93))
    print("Películas seleccionadas:")
    print("{}".format("-"*93))
    print()
    for i in range(len(peliculas_alquiladas)):
        print("{0:<3} {1:<50} {2:<12} {3:^12} {4:>11}".format("", peliculas_alquiladas[i].nombre, peliculas_alquiladas[i].genero, peliculas_alquiladas[i].anio, f"$ {peliculas_alquiladas[i].precio}"))
        print()
        sumar_precios += peliculas_alquiladas[i].precio
    print("{}".format("-"*93))
    print("{:>77} {:>14}".format("Total",f"$ {sumar_precios}"))
    print("{}".format("-"*93))

    print("Precione 0 para terminar")
    print("Precione 1 para agregar más películas")
    opcion = int(input("ingrese una opción: "))

    #Verificamos que el dato sea correcto
    while not opcion == 0 or opcion == 1:
        print()
        print("Por favor, ingrese un valor válido")
        opcion = int(input("ingrese una opción: "))

    if opcion == 0:
        print("Gracias por utilizar nuestro programa ¡Vuelva pronto!")
    elif opcion==1:
        alquilar_pelicula()
#--------------- FIN FUNCIÓN MOSTRAR FACTURA -----------------------------------

#======================= FIN ALQUILAR PELÍCULA =================================

#===================== INICIO FILTRADO DE PELÍCULAS ============================

#--------------------- INICO FUNCIÓN FILTRAR PELÍCULAS -------------------------
def filtrar_peliculas():
    # Llamada a la función de limpiar pantalla
    limpiar_pantalla()
    print("-----------------------------------------------------")
    print("------- Filtro de películas ------------- \n")
    print("Digite 1 para ver las peliculas según su genero")
    print("Digite 2 para ver las películas en un rango de precio")
    print("Digite 3 para ver las películas por año")
    print("Digite 4 para ver las peliculas por nombre")
    print("Ingrese 0 para volver")
    opcion = int(input("Por favor, digite una opción: "))

    if opcion == 0:
        menu()
    elif opcion == 1:
        input_string = input("Ingrese el genero que busca en nuestro catalogo: ")
        fil_gen(input_string)
    elif opcion == 2:
        opcion = int(input("Ingrese el precio máximo de alquiler (sin .): "))
        fil_pre(opcion)
    elif opcion == 3:
        opcion = int(input("Ingrese el año que desea consultar las peliculas: "))
        fil_anio(opcion)
    elif opcion == 4:
        opcion_submenu = input("Ingrese el nombre de la pelicula que busca (o una parte): ")
        fil_nombre(opcion)
#----------------------- FIN FUNCIÓN FILTRAR PELÍCULAS -------------------------

#---------------------- INICIO FUNCIÓN FILTRADO POR GÉNERO ---------------------
def fil_gen(inp):
    arr_filtro = []
    inp = inp.lower() #Convertimos cualquier cadena en minusculas
    inp = inp.capitalize() #Hacemos que se cambie la primera letra en mayusculas

    for i in range(len(arr_pelis)):
        if (arr_pelis[i].genero == inp):
            arr_filtro.append(arr_pelis[i].nombre)
    else:
        print()
        print("Coinciden", len(arr_filtro), "películas con:", "'"+inp+"'")
        print("-------------------------------------------------------")
        print()
        for j in range(len(arr_filtro)):
            print(f"\t {j + 1}", arr_filtro[j])
        print()

    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()
#------------------ FIN FUNCIÓN FILTRADO POR GÉNERO ----------------------------

#----------------- INICIO FUNCIÓN FILTRADO POR PRECIO --------------------------
def fil_pre(p_max):
    arr_filtro = []
    text_fil_pre = ""
    for i in range(len(arr_pelis)):
        if (arr_pelis[i].precio <= p_max):
            text_fil_pre = arr_pelis[i].nombre + " con el precio de: $" + str(arr_pelis[i].precio)
            arr_filtro.append(text_fil_pre)
    else:
        print()
        print("Coinciden", len(arr_filtro)," películas con precio menor o igual a:", p_max)
        print("---------------------------------------------------")
        print()
        for j in range(len(arr_filtro)):
            print(f"\t {j + 1}.", arr_filtro[j])
        print()

    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()
#------------------ FIN FUNCIÓN FILTRADO POR PRECIO ----------------------------

#------------------- INICIO FUNCIÓN FILTRADO POR AÑO ---------------------------
def fil_anio(anio):
    text_fil_an = ""
    arr_filtro = []
    for i in range(len(arr_pelis)):
        if (arr_pelis[i].anio == anio):
            text_fil_an = arr_pelis[i].nombre + " del año: " + str(arr_pelis[i].anio)
            arr_filtro.append(text_fil_an)
    else: 
        print()
        print("Coinciden", len(arr_filtro), "películas con:", anio)
        print("----------------------------------------------")
        print()
        for j in range(len(arr_filtro)):
            print(f"\t{j + 1}", arr_filtro[j])
        print()

    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()
#-------------------------- FIN FUNCIÓN FILTRADO POR AÑO -----------------------

#------------------------ INICIO FUNCIÓN FILTRADO POR NOMBRE -------------------   
def fil_nombre(nom):
    arr_filtro = []
    copy_arr = copy.deepcopy(arr_pelis)
    nom = nom.lower()
    for i in range(len(copy_arr)):
        copy_arr[i].nombre = copy_arr[i].nombre.lower()
        if (copy_arr[i].nombre.find(nom) >= 0 or copy_arr[i].nombre == nom):
            arr_filtro.append(arr_pelis[i].nombre)
    else:
        print()
        print("Coinciden", len(arr_filtro), "películas con:", "'" + nom + "'" )
        print("------------------------------------")
        print()
        for j in range (len(arr_filtro)):
            print(f"\t {j + 1}." , arr_filtro[j])
        print()

    del arr_filtro
    opcion_submenu = int(input("Digite 0 para volver: "))
    if opcion_submenu == 0: filtrar_peliculas()
#------------------------ FIN FUNCIÓN FILTRADO POR NOMBRE ----------------------

#========================= FIN FILTRADO DE PELÍCULAS ===========================

#============== INICIO PELÍCULAS DISPONIBLES ===========================
def peliculas_disponibles():
    limpiar_pantalla()
  
    #Creamos una tabla para mostrar las películas disponibles
    print("{}".format("-"*93))
    print("{0:<3} {1:<50} {2:<12} {3:^12} {4:>12}".format("Id","Título", "Género", "Año", "Precio"))
    print("{}".format("="*93))
    print()
    for i in range(len(arr_pelis)):
        print("{0:<3} {1:<50} {2:<12} {3:^12} {4:>11}".format(i+1,arr_pelis[i].nombre, arr_pelis[i].genero, arr_pelis[i].anio, f"$ {arr_pelis[i].precio}" ))
        print("{}".format("-"*93))

    pelicula_aleatoria()
# ==================== FIN PELÍCULAS DISPONIBLES =======================

#==================== INICIO MENÚ PRINCIPAL ========================
def menu():
    limpiar_pantalla()
    print("-----------------------------------------------------")
    print("------- Menú Principal -------------\n")
    print("Digite 1 para ver todas las películas disponibles")
    print("Digite 2 para filtrar las películas disponibles")
    print("Digite 3 para alquilar una película")
    print("Digite 0 para salir")
    opcion = int(input("Digite una opción: "))

    #Condición para mostrar el listado de películas
    if opcion == 1:
        peliculas_disponibles()
        print("Digite 1 si desea alquilar películas")
        print("Digite 0 si desea volver")
        opcion2 = int(input("Digite una opción: "))
        if opcion2 == 1:
            alquilar_pelicula()
        elif opcion2 ==0:
            menu()
    elif opcion == 2:
        filtrar_peliculas()
    elif opcion == 3:
        alquilar_pelicula()
    elif opcion == 0:
        print("Gracias por utilizar nuestro sistema, ¡vuelva pronto!")
#======================= FIN MENÚ PRINCIPAL ====================================

menu()