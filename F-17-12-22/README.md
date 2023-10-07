## Ejercicio 1
El juego de la sopa de letras se basa en una matriz de N x M (N y M enteros positivos mayores
a 1) donde hay que buscar palabras. Las palabras pueden aparecer escritas al derecho o al
revés y pueden estar ubicadas en forma vertical u horizontal dentro de la matriz, como puede
verse en la siguiente imagen.

<p align="center">
  <img width="200" src="https://github.com/ImNotGone/info-gnrl/blob/main/F-17-12-22/img-mat.jpeg">
</p>

Hacer un programa que invoque a una función jugar que reciba una matriz de letras y una
lista de palabras. La función deberá devolver dos listas, una con las palabras de la lista dada,
que sean encontradas en la matriz de letras y la otra con las que no se encontraron en ella.
La matriz de letras se encuentra en el archivo matriz.txt. El archivo se compone de N filas con
M letras cada una, y no es necesario validarlo. A continuación se ve un ejemplo del formato del
archivo.

```
SADASFJASDFJDIFSKRGMRSKGRMGMRGKRGRMGNEIREWSSW
SDVNCSIRKMGORNMGOEKGOKSCMSADEASKPWNWIFNWEFMWO
QEDMEOWDMEOWEMDOEWDMEOWDMWEODMEWODMEWODEMDOWE
```
La lista de palabras a buscar se encuentra en el archivo palabras.txt. El archivo se compone de
X palabras (siendo X entero positivo), una palabra por línea, y no es necesario validarlo. A
continuación se ve un ejemplo del formato del archivo.

```
PALABRA1
PALABRA2
PALABRA3
...
```
En caso de no encontrar ninguna de las palabras de la lista dada en la matriz, se debe devolver
una lista vacía y la otra con todas las palabras

### Ejemplo:

#### matriz.txt

```
ADCASAFG
ALACZEMR
OPSORTDA
```

#### palabras.txt
```
ORCA
MEZCAL
OCA
PERRO
CASA
AUTO
```

#### Palabras encontradas:
```
CASA
MEZCAL
OCA
```
#### Palabras no encontradas:
```
ORCA
PERRO
AUTO
```
## Ejercicio 2
El ADN es una molécula que se encuentra en el núcleo de las células y constituye el material
genético de los seres vivos, lo cual hace que cada ser vivo sea único.
Podemos pensar en el ADN como una cadena de caracteres. Los caracteres que aparecen en
esta secuencia serán siempre las mismas 4 letras :a,c,g,t, que representan los nucleótidos que
se usan para formar la cadena de ADN. Tres nucleótidos (Caracteres) consecutivos del ADN
codifican un determinado aminoácido, representado por una única letra del alfabeto inglés.
Usted debe realizar un programa en python que invoque a la función analizar_secuencia,
encargada de generar la secuencia de aminoácidos equivalente a una determinada secuencia
de ADN, de visualizarla en pantalla y de copiarla en un archivo de texto que llamará
secuenciaproteica.txt. Dicho archivo también deberá ser entregado en la actividad del final.
La función en cuestión deberá recibir como argumentos la secuencia de ADN a decodificar (un
string con solo letras) y la lista de los pares [nucleótidos, aminoácido] necesarios para la
decodificación (una lista de listas). Ver el ejemplo al final de enunciado
Cuando una dada secuencia de 3 nucleótidos no pueda ser decodificada, por no encontrarse en la
lista de listas de los pares, deberá mostrar en la secuencia de aminoácidos equivalente el caracter
‘?’, lo cual indica que hubo una mutación en el ADN y el aminoácido no podrá sintetizarse.
La información de la secuencia de ADN a transformar se encuentra en el archivo DNA.txt, el
cual lo podrá descargar del CAMPUS de la carpeta FINAL 17 DICIEMBRE.
La función a implementar en el programa es:

```py
analizar_secuencia (secuencia, listadecodificacion)
# secuencia: secuencia de caracteres ‘a’,’c’,’t’,‘g’ (string).
# listadecodificacion: pares nucleótidos-aminoacido [lista de listas]
```
#### Ejemplo 1:

Sí DNA.txt contiene la siguiente Secuencia de ADN (string):
`“attgaaacagtgagttcgtat”`
Para la lista de pares de decodificación:

```py
[['ATT','I'],['GAA','E'],['ACA','T'],['GTG','V'],['AGT','S'],['TAT','Y']]
```

La función debe generar la secuencia de aminoácidos: `IETVS?Y`

#### Ejemplo 2:

Sí DNA.txt contiene la siguiente Secuencia de ADN (string):
`“attgaaacagtgagttcgtat”`
Y la Lista de los pares es:
```py
[['TTT','F'],['TTC','F'],['TTA','L'],['TTG','L'],['TCT','S'],['TCC','S'],['TCA','S'],
['TAT','Y'],['TAC','Y'],['TAA','X'],['TAG','X'],['TGT','C'],['TGC','C'],['TGA','X'],
['TGG','W'],['CTT','L'],['CTC','L'],['CTA','L'],['CTG','L'],['CCT','P'],['CCC','P'],
['CCA','P'],['CCG','P'],['CAT','H'],['CAC','H'],['CAA','Q'],['CAG','Q'],['CGT','R'],
['CGC','R'],['CGA','R'],['CGG','R'],['ATT','I'],['ATC','I'],['ATA','I'],['ATG','M'],
['ACT','T'],['ACC','T'],['ACA','T'],['ACG','T'],['AAT','N'],['AAC','N'],['AAA','K'],
['AAG','K'],['AGT','S'],['AGC','S'],['AGA','R'],['AGG','R'],['GTT','V'],['GTC','V'],
['GTA','V'],['GTG','V'],['GCT','A'],['GCC','A'],['GCA','A'],['GCG','A'],['GAT','D'],
['GAC','D'],['GAA','E'],['GAG','E'],['GGT','G'],['GGC','G'],['GAG','G'],['GGG','G']]
```

La función debe generar la secuencia de aminoácidos: `IETVSLY`