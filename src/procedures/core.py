import random
import config.config as config
import procedures.checks as checks

#Representamos las direcciones con 🡳,🡲,🡶,🡵,🡱,🡷,🡰,🡴
#InsertarPalabra_random: List[List[char]] -> string -> List[string] -> int -> Any
#Los paramentos represental la sopa, la palabra a instertar, las direcciones posibles
# y si la palabra se puede cruzar con otras respectivamente,
# se retorna la posicion de la palabra si se pudo insertar y 1 de lo contrario
def InsertarPalabra_random(sopa, palabra, direcciones, cruce):
	dimension = len(sopa[0])
	coordenadas = [(x,y) for x in range(dimension) for y in range(dimension)] # Lista de posibles coordenadas
	random.shuffle(coordenadas) # Mezclo la lista de coordenadas
	ban = True

	# Mientras que haya coordenads posibles en la lista y no se haya insertado la palabra
	while ban and len(coordenadas)>0: 
		coord = coordenadas.pop()
		coord2 = coord # Variable auxiliar
		posibilidades = checks.Checks(coord, sopa, direcciones, palabra, cruce) # Posibles direcciones de la coordenada
		random.shuffle(posibilidades) # Mezclo las posibilidades

		if 0 < len(posibilidades): # Si hay alguna posible direccion
			for letra in palabra:
				sopa[coord[0]][coord[1]] = letra
				coord = config.mover(coord, posibilidades[0])
			ban = False

	if len(coordenadas) == 0: 
		return False # Si no hay mas posibles coordenadas

	return (coord2, palabra, posibilidades[0])


#InsertarPalabra_random: List[List[char]] -> string -> List[string] -> int -> Any
#Los paramentos represental la sopa, la palabra a instertar, las direcciones posibles
# y si la palabra se puede cruzar con otras respectivamente,
# Se retorna la sopa con las palabras o 0 si no se pudieron insertar
def JugarRandom(sopa, palabras, direcciones, cruce):
	MAX = config.variables['MAX_INTENTOS'] # Maximo numero de intentos randoms 
	insertadas = []
	i = 0
	while i in range(0, MAX):
		sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))] # Creo una copia de la sopa linea por linea
		for palabra in palabras:
			insertada = InsertarPalabra_random(sopa2, palabra, direcciones, cruce)
			if insertada == False:	
				i = 1 + i
				insertadas = []
				break
			else:
				insertadas.append(insertada)
		
		if insertadas and checks.CheckNoRepetidas(palabras, direcciones, (sopa2, insertadas)):
			return (sopa2, insertadas)
		else:
			insertadas = []

	if i == MAX:
		return False



#InsertarPalabra_metodico: List[List[char]] -> List[List[int]] -> List[(int, int)] -> List[string] -> List[string] -> int -> Any
#Los paramentos represental la sopa, los puntajes de las posiciones, la listas de las coordenadas
# la lista de las palabras no usadas, palabras insertadas, las direcciones posibles 
# y si la palabra se puede cruzar con otras respectivamente,
# Se retorna la sopa con las palabras o Falso si no se pudieron insertar
def InsertarPalabra_metodico(sopa, puntajes, coords, palabras, insertadas, direcciones, cruce):
	if len(palabras) == 0:
		if(checks.CheckNoRepetidas(palabras, direcciones, (sopa, insertadas))):
			return (sopa, insertadas)  # Si no hay mas palabras para insertar y no hay repetidas devuelvo la sopa
		else:
			return False
	for coord in coords:
		# Posibles direcciones de la coordenada
		posibilidades = checks.ChecksMetodico(coord, sopa, puntajes, direcciones, palabras[0], cruce)
		random.shuffle(posibilidades) # Mezclo las posibilidades
		for posibilidad in posibilidades: # Por cada posible direccion
			sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))] # Creo una copia de la sopa linea por linea
			insertadas2 = insertadas.copy() 
			aux = coord
			for letra in palabras[0]: # Inserto la palabra
				sopa2[aux[0]][aux[1]] = letra
				aux = config.mover(aux, posibilidad)
			insertadas2.append((coord, palabras[0], posibilidad))
			ban = InsertarPalabra_metodico(sopa2, puntajes, coords, palabras[1:], insertadas2, direcciones, cruce)
			
			if ban != False: return ban # Si no es falso entonces es la sopa completada

	return False
	

#InsertarPalabra_metodico: List[List[char]] -> List[string] -> List[string] -> int -> Any
#Los paramentos represental la sopa, la lista de las palabras a insertar, los puntajes de las posiciones
# las direcciones posibles y si la palabra se puede cruzar con otras respectivamente,
# Se retorna la sopa con las palabras o Falso si no se pudieron insertar
def JugarMetodico(sopa, palabras, puntajes, direcciones, cruce):
	Coords = []
	for x in range(len(sopa)):
		for y in range(len(sopa)):
			Coords.append( ((x,y), puntajes[x][y]) )

	Coords = sorted(Coords, key=config.second, reverse = True) # Ordeno de acuerdo al puntaje de la coordenada
	Coords = list(map(config.first, Coords)) # Saco el puntaje de la lista asi me queda las coordenadas ordenadas por el puntaje
   
    # Inserto todas las palabras en la sopa si se puede
	aux = InsertarPalabra_metodico(sopa, puntajes, Coords, palabras, [], direcciones, cruce) 
	if aux == False:
		return False
	else:
		return aux

#rellenar: List[List[char]] -> void
#Toma la sopa y le llena los espacios vacios con letras random
def rellenar(sopa):
	for V in range(len(sopa[0])):
		for H in range(len(sopa[0])):
			if sopa[V][H] == ' ':
				sopa[V][H] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def rellenarNoRepetidas(palabras, direcciones, SopaFinal):
	(sopa, insertadas) = SopaFinal
	sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))]
	rellenar(sopa2)
	while not checks.CheckNoRepetidas(palabras, direcciones, (sopa2, insertadas)):
		sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))]
		rellenar(sopa2)
	return (sopa2, insertadas)

#🡶.🡳.🡷
#🡲 - 🡰
#🡵.🡱.🡴

def inicio_juego(sopa, puntajes, palabras: list, dificultad: int):
	dificultad = int(dificultad)

	if dificultad == 0: dir = ["🡳","🡲"] 
	if dificultad == 1: dir = ["🡳","🡲","🡶"]    					  #Elijo la posibles direcciones
	if dificultad >= 2: dir = ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]

	cruce = True if dificultad == 3 else False

	palabras = sorted(palabras, key=len, reverse = True) # Ordeno las palabras de mayor a menor

	for i in range(len(palabras)):	# Hago las palabras mayusculas
		palabras[i] = palabras[i].upper()

	if not checks.ChecksPreliminares(palabras, len(sopa[0]), dificultad):
		return False 

	SopaFinal = JugarRandom(sopa, palabras, dir, cruce)
	if(SopaFinal != False):
		#print(SopaFinal[1])
		#config.imprimir_sopa(SopaFinal[0])
		SopaFinal = rellenarNoRepetidas(palabras, dir, SopaFinal) # Relleno la sopa
		return SopaFinal

	SopaFinal= JugarMetodico(sopa, palabras, puntajes, dir, cruce)
	if(SopaFinal == False):
		return False
	else:
		#config.imprimir_sopa(SopaFinal[0])
		SopaFinal = rellenarNoRepetidas(palabras, dir, SopaFinal) # Relleno la sopa
		return SopaFinal
