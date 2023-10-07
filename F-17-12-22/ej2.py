def importar_dna(nombre_archivo):
    # uso try - except para manejo de errores en caso de que no exista el archivo
    try:
        # abro el archivo para leer
        archivo = open(nombre_archivo, 'r')

        # me armo una lista en la cual voy a cargar de a 3 (osea x base)
        # las letras que encuentre en el archivo 
        lista = []
        for linea in archivo:
            # uso i, para mantener cuantas voy leyendo
            i = 0
            # uso 'cadena' como variable auxiliar para ir armando las bases
            cadena = ""
            for letra in linea:
                # como en la lista de decodificacion las bases estan en mayusc
                # paso la letra actual a mayusc antes de cargarla en la cadena
                cadena += letra.upper() 
                # incremento i
                i+=1
                # cada vez que i es 3, cargo la base 
                # formada por 3 letras en la lista de salida
                if(i == 3):
                    # agrego a la lista de bases la base actual
                    lista += [cadena]
                    # reinicio i en 0, para volver a empezar a contar
                    i = 0
                    # reinicio la cadena, para cargar la siguiente base
                    cadena = ""

        # cierro el archivo
        archivo.close()
        # retorno la lista de bases que encontre
        return lista
    
    # Si no pude abrir el archivo, aviso que no se encontro 
    # y cierro el programa con exit(1) para indicar error
    except FileNotFoundError:
        print(f"file {nombre_archivo} not found!")
        exit(1)

def decodificar(dna, lista_de_decodificacion):
    # inicio la cadena que voy a retornar como una cadena vacia
    decodificado = ""

    # busco para cada base en mi cadena de dna, su aminoacido
    for base in dna:
        # para cada base mantengo un estado
        # de si encontre o no su aminoacido
        # esto me sirve despues para ver si cargo el '?' o no
        encontre = False
        
        # En par tengo la base y el aminoacido
        # por ej: par = ['ATT', 'I']
        for par in lista_de_decodificacion:
            if(par[0] == base):
                decodificado += par[1]
                encontre = True
                # como ya encontre salgo del loop, para evitar seguir recorriendo
                break
        
        # Si no encontre -> marco el aminoacido como '?'
        if(not encontre):
            decodificado += '?'

    # retorno la cadena de aminoacidos
    return decodificado

# Ejemplo 1
nombre_archivo_dna = "DNA.txt"
dna = importar_dna(nombre_archivo_dna)
# print(dna)

lista_de_decodificacion = [['ATT','I'],['GAA','E'],['ACA','T'],['GTG','V'],['AGT','S'],['TAT','Y']]

aminoacidos = decodificar(dna, lista_de_decodificacion)
print(f" deberia ser IETVS?Y y es {aminoacidos}")

# Ejemplo 2
nombre_archivo_dna = "DNA2.txt"
dna = importar_dna(nombre_archivo_dna)
# print(dna)
lista_de_decodificacion = [['TTT','F'],['TTC','F'],['TTA','L'],['TTG','L'],['TCT','S'],['TCC','S'],['TCA','S'],
['TAT','Y'],['TAC','Y'],['TAA','X'],['TAG','X'],['TGT','C'],['TGC','C'],['TGA','X'],
['TGG','W'],['CTT','L'],['CTC','L'],['CTA','L'],['CTG','L'],['CCT','P'],['CCC','P'],
['CCA','P'],['CCG','P'],['CAT','H'],['CAC','H'],['CAA','Q'],['CAG','Q'],['CGT','R'],
['CGC','R'],['CGA','R'],['CGG','R'],['ATT','I'],['ATC','I'],['ATA','I'],['ATG','M'],
['ACT','T'],['ACC','T'],['ACA','T'],['ACG','T'],['AAT','N'],['AAC','N'],['AAA','K'],
['AAG','K'],['AGT','S'],['AGC','S'],['AGA','R'],['AGG','R'],['GTT','V'],['GTC','V'],
['GTA','V'],['GTG','V'],['GCT','A'],['GCC','A'],['GCA','A'],['GCG','A'],['GAT','D'],
['GAC','D'],['GAA','E'],['GAG','E'],['GGT','G'],['GGC','G'],['GAG','G'],['GGG','G']]

aminoacidos = decodificar(dna, lista_de_decodificacion)
# Este esta raro, porque la 6ta base en DNA2.txt es TCG y no aparece en la lista de decodificacion...
print(f" deberia ser IETVSLY y es {aminoacidos}")
