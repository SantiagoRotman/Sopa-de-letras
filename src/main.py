import os
import procedures.scripts as scripts 
import procedures.core as core  
import math

def main():
	Cpath = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input', 'entrada.c'))
	Lpath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'docs', 'lemario.txt'))
	
	(dimension, palabras, dificultad) = scripts.LeerSalidaC(Cpath, Lpath)
	dimension = int(dimension)

	sopa  = [[' ' for i in range(dimension)] for j in range(dimension)]

	sopa2 = [[i for i in range(dimension-j, math.floor(dimension/2)-j,-1)] + 
				[i for i in range(math.ceil(dimension/2)-j+1, dimension-j+1)] 
					for j in range(math.ceil(dimension/2))]

	for x in range(math.floor(dimension/2)-1, -1, -1):
		sopa2.append(sopa2[x])


	core.inicio_juego(sopa2, palabras, dificultad)


if __name__ == "__main__":
    main()