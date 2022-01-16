
def listas_a_checkear():
	pass
def CheckeEspacio(coord: (int, int)):
	pass
def CheckLetras():
	pass

def inicio_juego(lista, palabras: list, dificultad: int):
	thisdict = {
	  "🡱": 0,
	  "🡵": 1,
	  "🡲": 2,
	  "🡶": 3,
	  "🡳": 4,
	  "🡷": 5,
	  "🡰": 6,
	  "🡴": 7
	}
			
	palabras = sorted(palabras, key=len, reverse = True)
	