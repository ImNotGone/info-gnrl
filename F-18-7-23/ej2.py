# PROVINCIA,LOCALIDAD,LATITUD,LONGITUD,INAUGURACION,NORMA,NUMERO
def importar_csv(nombre_archivo):
    # uso try - except para manejo de errores en caso de que no exista el archivo
    try:
        # abro el archivo para leer
        archivo = open(nombre_archivo, "r")
        # inicio una lista vacia para cargar los datos del csv
        datos_csv = []
        # uso una variable auxiliar para saltearme la primera linea
        # la cual contiene el "header"
        es_la_primera_linea = True

        for linea in archivo:
            # si es la primera linea
            # pongo en falso la variable
            # sigo con la siguiente linea
            if(es_la_primera_linea):
                es_la_primera_linea = False
                continue

            # inicio una lista para cargar las columnas de la linea
            fila_actual = []
            # inicio una cadena vacia para ir cargando los caracteres
            columna_actual = ""
            for caracter in linea:
                # si el caracter es ',' se termino la columna
                if(caracter == ','):
                    # cargo la columna a la fila actual
                    fila_actual += [columna_actual]
                    # reinicio la cadena para cargar la siguiente columna
                    columna_actual = ""
                elif(caracter != '\n'):
                    # si la letra es != ',' y != al 'enter'
                    # entonces lo agrego a la columna
                    columna_actual += caracter

            # sumo la ultima columna a la fila actual
            fila_actual += [columna_actual]

            # sumo la fila actual a los datos del csv
            datos_csv += [fila_actual]

        # cierro el archivo
        archivo.close()
        # retorno los datos del csv
        return datos_csv
    
    # Si no pude abrir el archivo, aviso que no se encontro 
    # y cierro el programa con exit(1) para indicar error
    except FileNotFoundError:
        print(f"El archivo \"{nombre_archivo}\" no se pudo abrir")
        exit(1)

# dada una fecha en formato dd/mm/yyyy
# extraigo el yyyy
def obtener_anio(fecha):
    # cuento la cantidad de apariciones de '/'
    # para saber cuando tengo q empezar a acumular
    # el anio
    cont = 0
    anio = ""
    for letra in fecha:
        if(cont == 2):
            anio += letra
        if(letra == '/'):
            cont += 1
    return anio

# obtiene el anio ingresado por el usuario
# si el usuario ingresa un anio que no esta en 'anios_posibles'
# se le pide uno hasta que el mismo este contenido
def seleccionar_anio(anios_posibles):
    anio = input("Elija un anio: ")
    while(anio not in anios_posibles):
        print("No hay datos para ese anio, por favor seleccione otro")
        anio = input("Elija un anio: ")
    return anio

# dado el set de datos del csv de monumentos
# obtiene aquellos inaugurados en el anio pedido 
# ordenados por nombre de provincia
def obtener_inaugurados_en_anio(datos, anio):
    # inicio una lista vacia
    resultado = []

    for fila in datos:
        # el anio de la inauguracion debe ser igual al pedido
        if (obtener_anio(fila[4]) == anio):
            # en ese caso agrego esa fila a mi resultado
            resultado += [fila]

    # utilizo bubble-sort para
    # ordenar por nombre de provincia
    for i in range(len(resultado) - 1):
        for j in range(i+1, len(resultado)):
            nombre_i = resultado[i][0]
            nombre_j = resultado[j][0]
            if(nombre_i < nombre_j):
                aux = resultado[i]
                resultado[i] = resultado[j]
                resultado[j] = aux
    
    # retorno la lista de filas que cumplian
    # ordenada por nombre de provincia
    return resultado

# dedo el set de datos del csv de monumentos
# obtengo cuantos monumentos hay por provincia
# ordenado por cantidad de monumentos
def obtener_ranking_x_monumentos(datos):
    # inicio una lista vacia
    resultado = []

    for fila in datos:
        # mantengo un estado para ver si tengo que agregar
        # una provincia que no tenia antes, o si le incremente
        # el valor a una que ya tenia
        agregue = False
        # recorro la lista de resultados actuales
        for par in resultado:
            # si la provincia ya estaba en la lista
            if(par[0] == fila[0]):
                # incremento la cantidad de monumentos en esa provincia
                par[1] += 1
                # marco que ya estaba
                agregue = True
                # salgo del for, para no recorrer de mas
                break

        # si no estaba la agrego por primera vez, con el contador en 1
        if(not agregue):
            resultado += [[fila[0], 1]]

    # utilizo bubble-sort para
    # ordenar por cant
    for i in range(len(resultado) - 1):
        for j in range(i+1, len(resultado)):
            cant_i = resultado[i][1]
            cant_j = resultado[j][1]
            if(cant_i > cant_j):
                aux = resultado[i]
                resultado[i] = resultado[j]
                resultado[j] = aux

    # retorno la lista de prov, cant_monumentos
    # ordenada por cant_monumentos
    return resultado

nombre_archivo_datos = "monumentos.csv"
# PROVINCIA,LOCALIDAD,LATITUD,LONGITUD,INAUGURACION,NORMA,NUMERO
datos = importar_csv(nombre_archivo_datos)
# print(datos)

# a.
ranking = obtener_ranking_x_monumentos(datos)

# abro el archivo 'ranking.txt' para escritura
archivo = open("ranking.txt", 'w+')
# cargo todas las lineas del resultado
for par in ranking:
    archivo.write(f"{par[0]} {par[1]}\n")

# cierro el archivo
archivo.close()

# b.
# cargo todos los anios posibles en una lista
# podria ser un set, pero nose si excede la materia
anios_posibles = []
for fila in datos:
    anio = obtener_anio(fila[4])
    if (anio not in anios_posibles):
        anios_posibles += [anio]

# print(anios_posibles)

anio = seleccionar_anio(anios_posibles)

inaugurados_en_anio = obtener_inaugurados_en_anio(datos, anio)
print(inaugurados_en_anio)

# permite obtener un float a partir del input del usuario
# si es que el valor ingresado es correcto
# sino, imprime un mensaje y corta la ejecucion con exit(1)
def seleccionar_float(str):
    try:
        return float(input(f"Elija una {str}:"))
    except ValueError:
        print("La cordenada elegida no se pudo traducir a numero con coma")
        exit(1)

# le pide al usuario la latitud y longitud para retornarlas
def seleccionar_latitud_y_long():
    latitud = seleccionar_float("latitud")
    longitud = seleccionar_float("longitud")
    return (latitud, longitud)

# obtiene el monumento mas cercano a la latitud y longitud pedidas
def obtener_monumento_mas_cercano(datos, latitud, longitud):
    try:
        # creo variables para el resultado actual
        # y la distancia de el resultado actual
        resultado = None
        distancia_res = None
        for fila in datos:
            latitud_2 = float(fila[2])
            longitud_2 = float(fila[3])
            distancia = ((latitud_2-latitud)**2 + (longitud_2-longitud) **2) ** (1/2)
            # si la distancia_res es None -> no cargue ninguno todavia
            # si la distancia_res es > distancia -> tengo que actualizar el actual
            # si la distancia_res es = distancia -> tengo que agregar ese a el resultado tambien 
            if(distancia_res == None or distancia_res >= distancia):
                # si es None o si es != (por lo tanto >)
                # piso el resultado con la fila actual
                if(distancia_res == None or distancia_res != distancia):
                    resultado = [fila]
                # si no -> son = por lo tanto agrego la fila al resultado
                else:
                    resultado += [fila]
                # actualizo la distancia a la cual se encuentran los resultados actuales
                distancia_res = distancia

        # retorno lo que haya quedado en resultado
        return resultado
    except ValueError:
        print("No se pudo traducir una de las latitudes/longitudes en los datos a float")
        exit(1)

# c.
(latitud, longitud) = seleccionar_latitud_y_long()

monumento_mas_cercano = obtener_monumento_mas_cercano(datos, latitud, longitud)
print(monumento_mas_cercano)