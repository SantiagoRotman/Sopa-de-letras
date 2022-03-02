# Sopa De Letras

TP2 prog de Santiago Nicolas Rotman

## Descripcion

Este programa elije n palabras distintas de un lemario y luego crea una sopa de letras con ellas. 

### Pre-requisitos 📋

Se necesita solamente gcc y pyhton para ejecutar este programa


## Ejecutando las pruebas ⚙️

Explica como ejecutar las pruebas automatizadas para este programa

### C

```
cd src/input
gcc assert.c
./a.out
```

### Python

```
cd src/
python -m pytest ../
```

## Ejecutando el programa

Ejecutar el programa es muy sencillo, veamos

```
cd src/
python main.py <lemario> <dimension> <Cant Palabras> <dificultad>
```
Las variables representan:
* lemario: El nombre del archivo del lemario, debe estar en /docs

* dimension: El largo de la sopa de letras
  
* Cant Palabras: La cantidad de palabras en la sopa
  
* dificultad: Un numero entre 0 y 3
  * 0: Fácil. Sólo palabras horizonatales de izquierda a derecha y verticales de arriba a abajo.
  * 1: Medio. Palabras horizontales de izquierda a derecha, verticales de arriba a abajo o diagonales de esquina superior izq a esquina inferior derecha.
  * 2: Difícil. Palabras en horizonal, vertical o diagonal sin restricciones.
  * 3: Muy difícil. Se agrega la posibilidad de que las palabras se puedan cortar, es decir, puedan compartir letras.

## Ejemplo
```
cd src/
python main.py lemario.txt 20 10 3
```
Salida, se imprime en un archivo llamado SopaFinal.txt
```
Sopa de Letras
BPLUCJSBWNKXHEDQWOSR
TTJDBECDFHXALERPDPUA
ZAZICYOYKHZHALWIMLQF
MQBMCLNRJGOBIERNAVBT
RESPPLASKYHLAURTSEMZ
HNWRKLUALYWAEWTRTPCB
ECKEXLFKZAXMQVXOFHUT
GUGCRODACINUMOCRETNI
BKWIAPZZRDGMTLSVWXNT
RLASSQLJLJITRYECKROR
XSQOANTEDILUVIANOLOY
MUTODANIPONIMKSOIMND
RFZQALPBANMZJDBFLGAR
ZLLYDQEWTNOPWNOSBPXC
CHKUUONFJJLEIRQKZDZO
NOICANEGIXOABNBQFZNJ
WTTPLYDYFCSMLWPJGUXE
DUXWLDPLGPIPLJDPUDRC
ZRWIYZTXRTHZFSFKKRBD
QDGMVLTWIHOIWRCTFGHH

```
## Configurar el programa
La configuracion se encuentra src/config/config.py
* Se pueden cambiar los nombres de los archivos 
* Se puede cambiar el maximo numero de intentos de la funcion random  
* Se pueden cambiar las direcciones posibles de cada dificultad 
