import subprocess
import os

def LeerSalidaC(Cpath: str, Lpath: str):
	EXEpath = os.path.realpath(os.path.join('.', os.path.dirname(__file__), '..', 'a.out'))
	OUTpath = os.path.realpath(os.path.join('.', os.path.dirname(__file__), '..', 'out.txt'))
	

	subprocess.Popen(['gcc', '-lm', Cpath])
	if subprocess.call([EXEpath, Lpath, '50', '6', '5']):
		print("error en la entrada")
		return 1

	palabras = []
	with open(OUTpath, 'r') as salida:
		salida.readline() 
		dimension = salida.readline().strip('\n')
		salida.readline()

		for linea in salida:
			linea = linea.strip('\n')
			if linea == 'COMPLEJIDAD':
				break
			palabras.append(linea)
		dificultad = salida.readline().strip('\n')

	return (dimension, palabras, dificultad)
