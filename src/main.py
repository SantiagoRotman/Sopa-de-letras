import os
import procedures.scripts as scripts 
import procedures.core as core  


def main():
	Cpath   = os.path.realpath(os.path.join(os.path.dirname(__file__), 'input', 'entrada.c'))
	Lpath   = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'docs', 'lemario.txt'))
	
	(dimension, palabras, dificultad) = scripts.LeerSalidaC(Cpath, Lpath)
	sopa = [[' ' for i in range(int(dimension))]for j in range(int(dimension))]

	core.inicio_juego(sopa, palabras, dificultad)


if __name__ == "__main__":
    main()