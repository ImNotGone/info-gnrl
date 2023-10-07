## Ejercicio 1
En un deposito operado por robots, las cajas se almacenan sobre distinas plataformas numeradas que comienzan en 1. 
La siguiente plataforma es la 2 y asi sucesivamente.
Se debe tener en cuenta que no se conoce la cantidad total de plataformas.

Cada dia se recibe un envio de cajas que deben almacenarse en las plataformas.
Cada caja posee un peso dado, que se indica por medio de un numero entero.

#### Ejemplo
Un envio podria ser:
```py
envio_1 = [5, 2, 3]
```
Lo que representa 3 cajas, donde:
 - la primera caja (de peso 5Kg), le corresponde a la plataforma 1,
 - la siguiente caja, de 2Kg, la plataforma 2
 - y por ultimo la caja de 3Kg, la plataforma 3

Al recibir un nuevo encio, los robots tratan de acomodar las cajas nuevas en las plataformas con los envios anteriores con el siguiente problema:
Al apoyar una caja sobre otra caja de menor peso, la caja de abajo se destruye y desaparece, y la caja de arriba cae hasta llegar a la plataforma o encontrar una caja cuyo peso sea mayor o igual.

Se asume que el deposito inicialmente esta vacio, o sea, sin cajas.

#### Ejemplo
Entonces el deposito tras el primer envio, queda de la siguiente manera:
```
           5 2 3
Plataforma 1 2 3 4 ...
```
Si ahora llega un nuevo envio
```py
envio_2 = [2, 4]
```
Entonces:
 - la caja de peso 2Kg va a la plataforma 1, y se apoya sobre la de 5Kg del envio anterior,
 - la caja de peso 4Kg va a la plataforma 2, pero aplasta la caja de peso 2Kg, de modo que el nuevo estado del deposito seria:
```
           2
           5 4 3
Plataforma 1 2 3 4 ...
```

*Hacer una funcion llamada* "`mi_deposito`" que reciba como argumento los envios de cajas de varios dias (una lista de cajas por envio) 
*y devuelva el estado final de cada plataforma en una lista de listas*, donde cada fila presenta las cajas de cada una de las plataformas 
(caja de mas abajo en la pos 0):

#### Ejemplo 1
Usando el caso antes visto
```py
envios = [ [5, 2, 3], [2, 4] ]
mi_deposito(envios)
```
Debe devolver:
```py
[ [5, 2], [4], [3] ]
```
Donde:
 - `[5, 2]`, corresponde a los pesos de las cajas en la plataforma 1
 - `[4]`, el peso de la caja en la plataforma 2
 - `[3]`, el peso de la caja en la plataforma 3

#### Ejemplo 2
```py
envios = [ [5, 3, 2], [2, 4], [1, 3, 5]]
mi_deposito(envios)
```
Debe devolver:
```py
[ [5, 2, 1], [4, 3], [6] ]
```
Donde:
 - `[5, 2, 1]`, corresponde a los pesos de las cajas en la plataforma 1
 - `[4, 3]`, el peso de las cajas en la plataforma 2
 - `[6]`, el peso de la caja en la plataforma 3

## Ejercicio 2
El archivo `monumentos.csv` contiene informacion sobre lugares y monumentos historicos en todo el pais.
Es cun archivo de tipo CSV que contient los siguientes campos, niguno de los cuales esta vacio:
```
PROVINCIA, LOCALIDAD, LATITUD, LONGITUD, INAUGURACION, NORMA, NUMERO
```
 - Las columnas LATITUD y LONGITUD contienen un numero de tipo float con 8 decimales
 - La columna INAUGURACION representa una fecha en el formato `dia/mes/anio` donde `dia` y `mes` le pueden corresponder 1 o 2 caracteres, y anio siempre tiene 4 caracteres.
 - La columna NORMA solo puede tener 2 calores, 'Decreto' o 'Ley'
 - Y por ultimo NUMERO representa un entero positivo, el numero de la norma correspondiente.

Se requiere un programa para procesar esta informacion a traves de las siguientes funcionalidades:

 a. Guardar en un archivo de texto llamado `ranking.txt` un ranking de provincias, ordenadas de menor a mayor por cantidad de monumentos.
 Ejemplo de formato de escritura en el archivo:
 ```
 BUENOS AIRES 33
 CORDOBA 45
 MENDOZA 80
 ```
 
 b. Generar y mostrar una lista de todos los monumentos/sitios historicos inaugurados en un anio ingresado por el usuario, ordenados por el nombre de la provincia en orden alfabetico descendente (Z-A o z-a).
 Si para el anio ingresado no hay registros se debe informar al usuario y darle la opcion de ingresar otro.

 c. Preguntar al usuario una latitud (latitud1) y una longitud (longitud1). Encotrar  el monumento mas cercano y mostrarlo por pantalla. Si hay mas de uno a igual distancia mostrarlos todos. La visualizacion debe incluir: `Provincia`, `Localidad` y `Distancia` calculada.
 Para calcular la distancia, la aproximamos por la distancia en el plano:
  
  Dados dos puntos con coordeadas (latitud1, longitud1) y (latitud2, longitud2)
 ```py
 distancia = ((latitud2-latitud1)**2 + (longitud2-longitud1)**2) ** 1/2
 ```
 