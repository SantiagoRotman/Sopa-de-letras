import procedures.scripts as scripts 
import procedures.core as core  
import config.config as config
import os, sys
import math


def main(argv):
	archivos = config.archivos
	Cpath = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input', archivos["entradaC"]))
	Lpath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'docs', archivos["lemario"]))
	
	(dimension, palabras, dificultad) = scripts.LeerSalidaC(argv, Cpath, Lpath) # Ejecuto el programa de c
	dimension = int(dimension)

	# Creo la sopa como un array bidimensional relleno de espacios
	sopa  = [[' ' for i in range(dimension)] for j in range(dimension)]

	#  5 4 3 4 5
	#  4 3 2 3 4 ejemplo para dimension = 5
	#  3 2 1 2 3
 	# Creo un array bidimensional con los puntajes de cada celda
	puntajes = [[i for i in range(dimension-j, math.floor(dimension/2)-j,-1)] +   
					[i for i in range(math.ceil(dimension/2)-j+1, dimension-j+1)] 
						for j in range(math.ceil(dimension/2))]

	#  5 4 3 4 5
	#  4 3 2 3 4
	#  3 2 1 2 3 ejemplo para dimension = 5
	#  4 3 2 3 4
	#  5 4 3 4 5
	# Espejo el array de puntajes
	for x in range(math.floor(dimension/2)-1, -1, -1): 
		puntajes.append(puntajes[x])


	SopaFinal = core.inicio_juego(sopa, puntajes, palabras, dificultad)

	if SopaFinal:
		scripts.SalidaSopa(SopaFinal)
	else:
		scripts.SalidaImposible(SopaFinal)

if __name__ == "__main__":
    main(sys.argv[1:])