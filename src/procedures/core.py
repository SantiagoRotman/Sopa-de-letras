import random
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
		posibilidades.append("🡶") if (dimension-x > largo and dimension-y > largo) else None

	if "🡵" in direcciones:
		posibilidades.append("🡵") if (x > largo and dimension-y > largo) else None

	if "🡱" in direcciones:
		posibilidades.append("🡱") if (0 <= x-largo) else None

	if "🡷" in direcciones:
		posibilidades.append("🡷") if (dimension-x > largo and y > largo) else None

	if "🡰" in direcciones:
		posibilidades.append("🡰") if (0 <= y-largo) else None

	if "🡴" in direcciones:
		posibilidades.append("🡴") if (x > largo and y > largo) else None

	return posibilidades


def CheckLetras(palabra, listas, cruce: bool):
	direcciones = []
	for key in listas.keys():
		ban = all(((type(letra2) is int) or (letra1 == letra2 and cruce)) for  letra1, letra2 in zip(palabra, listas[key]))
		if ban:
			direcciones.append(key) 
	return direcciones


def Checks(coord: (int, int), sopa, direcciones, palabra, cruce):
	direcciones = CheckEspacio(coord, direcciones, len(sopa[0]), len(palabra))
	listas = listas_a_checkear(coord, sopa, direcciones, len(palabra))
	direcciones = CheckLetras(palabra, listas, cruce)

	return direcciones


def InsertarPalabra_random(sopa, palabra, direcciones, cruce):
	dimension = len(sopa[0])
	coordenadas = [(x,y) for x in range(dimension) for y in range(dimension)]
	random.shuffle(coordenadas)
	ban = True
	while ban and len(coordenadas)>0:
		coord = coordenadas.pop()
		coord2 = coord
		posibilidades = Checks(coord, sopa, direcciones, palabra, cruce)

		if 0 < len(posibilidades):
			random.shuffle(posibilidades)
			for letra in palabra:
				sopa[coord[0]][coord[1]] = letra
				coord = mover(coord, posibilidades[0])
			ban = False
		
	if len(coordenadas) == 0: 
		return 1

	print(coord2, palabra, posibilidades[0])
	return 0


def JugarRandom(sopa, palabras, direcciones, cruce):
	i = 0
	while i in range(0, 20):
		sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))]
		print(i)
		for palabra in palabras:
			ban = InsertarPalabra_random(sopa2, palabra, direcciones, cruce)
			if ban:	
				i = 1 + i
				break
		if not ban:
			rellenar(sopa2)
			config.imprimir_sopa(sopa2)
			return sopa2

	if i == 20:
		print ("no se pudo")

def InsertarPalabra_metodico(sopa, coords, palabra, direcciones, cruce):
	dimension = len(sopa[0])
	


def JugarMetodico(sopa, palabras, direcciones, cruce):
	Coords = []
	for x in range(len(sopa)):
		for y in range(len(sopa)):
			Coords.append( ((x,y), sopa[x][y]) )

	Coords = sorted(Coords, key=config.second, reverse = True)
	
	for palabra in palabras:


def rellenar(sopa):
	for V in range(len(sopa[0])):
		for H in range(len(sopa[0])):
			if type(sopa[V][H]) is int:
				sopa[V][H] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


#🡶.🡳.🡷
#🡲 - 🡰
#🡵.🡱.🡴

def inicio_juego(sopa, palabras: list, dificultad: int):
	dificultad = int(dificultad)

	if dificultad == 0:
		dir = ["🡳","🡲"] 
	if dificultad == 1:
		dir = ["🡳","🡲","🡶"]  
	if dificultad >= 2:
		dir = ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]
	cruce = True if dificultad == 3 else False

	palabras = sorted(palabras, key=len, reverse = True)

	for i in range(len(palabras)):
		palabras[i] = palabras[i].upper()

	

	JugarRandom(sopa, palabras, dir, cruce)
	JugarMetodico(sopa, palabras, dir, cruce)
