
from math import ceil
import config.config as config

def FiltrarDirecciones(posibilidades):
	direcciones = []
	for (key, value) in posibilidades.items():
	    if value:
	        direcciones.append(key)
	return direcciones


def mover(coord:(int, int), direccion):
	(x, y) = coord
	if "🡳" == direccion: return (x+1,  y )
	if "🡲" == direccion: return ( x , y+1)
	if "🡶" == direccion: return (x+1, y+1)
	if "🡵" == direccion: return (x-1, y+1)
	if "🡱" == direccion: return (x-1,  y )
	if "🡷" == direccion: return (x+1, y-1)
	if "🡰" == direccion: return ( x , y-1)
	if "🡴" == direccion: return (x-1, y-1)


def listas_a_checkear(coord: (int, int), sopa, direcciones, largo: int):
	listas = dict()

	for dir in direcciones:
		aux = []
		coord2 = coord

		for i in range(largo):
			aux.append(sopa[coord2[0]][coord2[1]])
			coord2 = mover(coord2, dir)

		listas[dir] = aux

	return listas


def CheckEspacio(coord: (int, int), direcciones, dimension: int, largo: int):
	(x,y) = coord
	posibilidades = []

	if "🡳" in direcciones:
		posibilidades.append("🡳") if (dimension >= x+largo) else None

	if "🡲" in direcciones:
		posibilidades.append("🡲") if (dimension >= y+largo) else None

	if "🡶" in direcciones:
		posibilidades.append("🡶") if (dimension-x >= largo and dimension-y >= largo) else None

	if "🡵" in direcciones:
		posibilidades.append("🡵") if (x >= largo and dimension-y >= largo) else None

	if "🡱" in direcciones:
		posibilidades.append("🡱") if (0 <= x-largo) else None

	if "🡷" in direcciones:
		posibilidades.append("🡷") if (dimension-x >= largo and y >= largo) else None

	if "🡰" in direcciones:
		posibilidades.append("🡰") if (0 <= y-largo) else None

	if "🡴" in direcciones:
		posibilidades.append("🡴") if (x >= largo and y >= largo) else None

	return posibilidades


def CheckLetras(palabra, listas, cruce: bool):
	direcciones = []
	for key in listas.keys():
		ban = all((letra2 == ' ' or (letra1 == letra2 and cruce)) for  letra1, letra2 in zip(palabra, listas[key]))
		if ban:
			direcciones.append(key) 
	return direcciones

def CheckPuntaje(coord: (int, int), puntajes, direcciones, largo):
	aux  = list()
	aux2 = list()
	largo -= 1
	(x,y) = coord
	if "🡳" in direcciones: aux.append(("🡳", puntajes[x+largo][y]   ))
	if "🡲" in direcciones: aux.append(("🡲", puntajes[ x ][y+largo] ))
	if "🡱" in direcciones: aux.append(("🡱", puntajes[x-largo][ y ] ))
	if "🡰" in direcciones: aux.append(("🡰", puntajes[ x ][y-largo] ))
	if "🡶" in direcciones: aux2.append(("🡶", puntajes[x+largo][y+largo] ))
	if "🡷" in direcciones: aux2.append(("🡷", puntajes[x+largo][y-largo] ))
	if "🡵" in direcciones: aux2.append(("🡵", puntajes[x-largo][y+largo] ))
	if "🡴" in direcciones: aux2.append(("🡴", puntajes[x-largo][y-largo] ))

	aux = sorted(aux, key=config.second, reverse = True)
	aux2 = sorted(aux2, key=config.second, reverse = True)
	return list(map(config.first, aux)) + list(map(config.first, aux2))



def ChecksMetodico(coord: (int, int), sopa, puntajes, direcciones, palabra, cruce):
	direcciones = CheckEspacio(coord, direcciones, len(sopa[0]), len(palabra))
	listas = listas_a_checkear(coord, sopa, direcciones, len(palabra))
	direcciones = CheckLetras(palabra, listas, cruce)
	direcciones = CheckPuntaje(coord, puntajes, direcciones, len(palabra))

	return direcciones

def Checks(coord: (int, int), sopa, direcciones, palabra, cruce):
	#print(direcciones)
	direcciones = CheckEspacio(coord, direcciones, len(sopa[0]), len(palabra))
	#print(direcciones)
	listas = listas_a_checkear(coord, sopa, direcciones, len(palabra))
	#print(listas)
	direcciones = CheckLetras(palabra, listas, cruce)



	return direcciones
