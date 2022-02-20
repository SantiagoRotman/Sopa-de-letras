import random
from re import A
from turtle import pos
import config.config as config
import procedures.checks as checks

def InsertarPalabra_random(sopa, palabra,  direcciones, cruce):
	dimension = len(sopa[0])
	coordenadas = [(x,y) for x in range(dimension) for y in range(dimension)]
	random.shuffle(coordenadas)
	ban = True
	while ban and len(coordenadas)>0:
		coord = coordenadas.pop()
		coord2 = coord
		posibilidades = checks.Checks(coord, sopa, direcciones, palabra, cruce)

		if 0 < len(posibilidades):
			random.shuffle(posibilidades)
			for letra in palabra:
				sopa[coord[0]][coord[1]] = letra
				coord = checks.mover(coord, posibilidades[0])
			ban = False
		
	if len(coordenadas) == 0: 
		return 1

	print(coord2, palabra, posibilidades[0])
	return 0


def JugarRandom(sopa, palabras, direcciones, cruce):
	i = 0
	MAX = config.variables['MAX_INTENTOS']
	while i in range(0, MAX):
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

	if i == MAX:
		print ("no se pudo")




def InsertarPalabra_metodico(sopa, puntajes, coords, palabras, direcciones, cruce):
	if len(palabras) == 0: return sopa
	#print(len(palabras)) 
	for coord in coords:
		#print(coord)
		posibilidades = checks.ChecksMetodico(coord, sopa, puntajes, direcciones, palabras[0], cruce)
		#print(posibilidades)
		for posibilidad in posibilidades:
			#print("aaaa")
			sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))]
			aux = coord
			#print(palabras[0], posibilidad, coord)
			for letra in palabras[0]:
				sopa2[aux[0]][aux[1]] = letra
				aux = checks.mover(aux, posibilidad)

			ban = InsertarPalabra_metodico(sopa2, puntajes, coords, palabras[1:], direcciones, cruce)
			
			if ban != False: return ban

	return False
	


def JugarMetodico(sopa, palabras, puntajes, direcciones, cruce):
	Coords = []
	for x in range(len(sopa)):
		for y in range(len(sopa)):
			Coords.append( ((x,y), puntajes[x][y]) )

	Coords = sorted(Coords, key=config.second, reverse = True)
	Coords = list(map(config.first, Coords))
   
	aaa = InsertarPalabra_metodico(sopa, puntajes, Coords, palabras, direcciones, cruce)
	if aaa == False:
		print("no se pudo")
	else:
		config.imprimir_sopa(aaa)


def rellenar(sopa):
	for V in range(len(sopa[0])):
		for H in range(len(sopa[0])):
			if sopa[V][H] == ' ':
				sopa[V][H] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


#🡶.🡳.🡷
#🡲 - 🡰
#🡵.🡱.🡴

def inicio_juego(sopa, puntajes, palabras: list, dificultad: int):
	dificultad = int(dificultad)

	if dificultad == 0:
		dir = ["🡳","🡲"] 
	if dificultad == 1:
		dir = ["🡳","🡲","🡶"]  
	if dificultad >= 2:
		dir = ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]
	cruce = True if dificultad == 3 else False

	palabras = sorted(palabras, key=len, reverse = True)
	print(palabras)
	for i in range(len(palabras)):
		palabras[i] = palabras[i].upper()

	

	JugarRandom(sopa, palabras, dir, cruce)
	print("")
	JugarMetodico(sopa, palabras, puntajes, dir, cruce)
