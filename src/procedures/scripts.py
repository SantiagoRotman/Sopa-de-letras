import config.config as config
import subprocess
import os, sys
 

#LeerSalidaC -> string -> string -> (int, List[string], int)
def LeerSalidaC(argv, Cpath: str, Lpath: str):
	archivos = config.archivos
	subprocess.run(['gcc', '-lm', Cpath])   # Compila el programa de C

	EXEpath = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', archivos["C_Linux"]))
	
	if subprocess.call([EXEpath, Lpath, argv[1], argv[2], argv[3] ]):  # Ejecuto el programa compilado y si 
		print("error en la entrada")
		sys.exit(2)

	OUTpath = os.path.realpath(os.path.join('.', os.path.dirname(__file__), '..', archivos["salidaC"]))
	palabras = []
	with open(OUTpath, 'r') as salida: # Leo el archivo de salida
		salida.readline() # Leo basura
		dimension = salida.readline().strip('\n')
		salida.readline() # Leo basura

		for linea in salida: # Leo las palabras
			linea = linea.strip('\n')
			if linea == 'COMPLEJIDAD':
				break
			palabras.append(linea)
		dificultad = salida.readline().strip('\n')

	return (dimension, palabras, dificultad)

def SalidaError():
	pass

def SalidaImposible():
	f = open("SopaFinal.txt", "w")
	f.write("Sopa de Letras\n")
	f.write("No se puede crear\n")


def SalidaSopa(sopaFinal):
	(sopa, palabras) = sopaFinal
	f = open("SopaFinal.txt", "w")
	f.write("Sopa de Letras\n")
	for line in sopa:
		f.write("".join(line)+"\n")



