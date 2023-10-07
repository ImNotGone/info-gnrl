def importar_lineas(nombre_archivo):
    # uso try - except para manejo de errores en caso de que no exista el archivo
    try:
        # abro el archivo para leer
        archivo = open(nombre_archivo, 'r')
        # armo una lista para cargar cada linea del archivo
        lista = []

        # para cada linea del archivo
        for linea in archivo:
            # inicio una cadena vacia
            cadena = ""
            # por cada letra de la linea actual, 
            # agrego todas menos el 'enter' 
            for letra in linea:
                if(letra != '\n'):
                    cadena += letra
            # guardo la linea actual (sin el 'enter') en la lista
            lista += [cadena]

        # cierro el archivo
        archivo.close()
        # retorno la lista de lineas del archivo
        return lista
    
    # Si no pude abrir el archivo, aviso que no se encontro 
    # y cierro el programa con exit(1) para indicar error
    except FileNotFoundError:
        print(f"file {nombre_archivo} not found!")
        exit(1)

def matchea_palabra(matriz, i, j, palabra, direccion):
    len_palabra = len(palabra)
    cant_filas = len(matriz)
    cant_cols = len(matriz[0])
    # en k, recorro la palabra,
    # a partir de i e j recorro la matriz
    k = 0
    while(k < len_palabra):
        # si me fui de la matriz en i o en j o 
        # si la letra actual de la matriz no coincide con la letra actual de la palabra
        # retorno falso
        if(i < 0 or i >= cant_filas or j < 0 or j >= cant_cols or matriz[i][j] != palabra[k]):
            return False
        # sino, sigo recorriendo
        # incremento k
        k += 1
        # muevo i segun direccion actual
        i += direccion[0]
        # muevo j segun direccion actual
        j += direccion[1]

    # si k llego a 'len_palabra'
    # entonces la palabra estaba contenida en la matriz 
    # con la direccion actual
    # por lo tanto retorno verdadero
    return True

def palabra_esta_en_matriz(matriz, palabra):
    # para fijarme si la palabra se encuentra en la matriz, 
    # recorro en todas las direcciones
    # izq, der, arriba, abajo y en las 4 diagonales
    direcciones = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    # recorro la matriz x filas y columnas
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            # primero me fijo si la primera letra de la palabra
            # coincide con la posicion actual de la matriz
            if(matriz[i][j] == palabra[0]):
                # en caso de que coincida, me fijo en las 8 direcciones
                # si la palabra se encuentra en alguna de ellas
                for direccion in direcciones:
                    # si esta, retorno verdadero
                    if(matchea_palabra(matriz, i, j, palabra, direccion)):
                        return True
                    
    # si recorri TODA la matriz y no encontre la palabra
    # retorno falso
    return False


def jugar(matriz, palabras):
    # Creo 2 listas para devolver
    # las palabras encontradas
    # y las no encontradas
    palabras_encontradas = []
    palabras_no_encontradas = []
    
    # por cada palabra en la lista de palabras
    for palabra in palabras:
        # si la palabra se encontraba en la matriz
        # la cargo en palabras encontradas
        # sino, en palabras no encontradas
        if (palabra_esta_en_matriz(matriz, palabra)):
            palabras_encontradas += [palabra]
        else:
            palabras_no_encontradas += [palabra]

    # retorno ambas listas
    return (palabras_encontradas, palabras_no_encontradas)

nombre_archivo_matriz = "matriz.txt"
matriz = importar_lineas(nombre_archivo_matriz)
# print(matriz)

nombre_archivo_palabras = "palabras.txt"
palabras = importar_lineas(nombre_archivo_palabras)
# print(palabras)

(palabras_encontradas, palabras_no_encontradas) = jugar(matriz, palabras)
print(palabras_encontradas)
print(palabras_no_encontradas)

# Ejemplo
nombre_archivo_matriz = "matriz1.txt"
matriz = importar_lineas(nombre_archivo_matriz)
# print(matriz)

nombre_archivo_palabras = "palabras1.txt"
palabras = importar_lineas(nombre_archivo_palabras)
# print(palabras)

(palabras_encontradas, palabras_no_encontradas) = jugar(matriz, palabras)
print(palabras_encontradas)
print(palabras_no_encontradas)

