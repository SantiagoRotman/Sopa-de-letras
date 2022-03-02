from math import ceil
import config.config as config


#listas_a_checkear: (int, int) -> List[List[char]] -> List[string] -> int -> dict[string][List(char)]
#Los argunetos representan la coordenada, la sopa, las direcciones posibles y el largo de la palabra
# devuelve el diccionario con la claves siendo las direcciones y las varibles son las listas de las 
# celdas en la direccion y hasta el largo de la palabra 
#
#				 ['A'|' '|'Z']
#Entrada: (0,0), [' '|'B'|' '], ["🡳","🡲","🡶"], 3, Salida: {"🡳":['A',' ','x'],"🡲":['A',' ','Z'],"🡶":['A','B','B']}
#				 ['X'|' '|'B']
def listas_a_checkear(coord: (int, int), sopa, direcciones, largo: int):
	listas = dict()
	for dir in direcciones:
		aux = []
		coord2 = coord

		for i in range(largo):
			aux.append(sopa[coord2[0]][coord2[1]])
			coord2 = config.mover(coord2, dir)
		listas[dir] = aux

	return listas


#CheckEspacio: (int, int) -> List[string] -> int -> int -> Lista[string]
# devuelve la listas de las direcciones para las cuales la palabra entra
#
#Entrada: (2,1), ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], 5, 3, Salida ["🡳","🡲","🡶","🡵","🡱"]
#
def CheckEspacio(coord: (int, int), direcciones, dimension: int, largo: int):
	(x,y) = coord
	dimension = dimension-1
	largo = largo-1
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


#CheckLetras: string -> dict[string][List(char)] -> Bool -> List(string)
#Toma la palabra, el diccionario con la claves siendo las direcciones y las varibles son las listas de las 
# celdas en la direccion y hasta el largo de la palabra y si se puede cruzar con otras
# devuelve las direcciones que no tenga letras en su trayectoria o que la las letras de la palabra
# sean iguales a las letra que estan en la trayectoria
#
# Entrada: "ABB", {"🡳":['A', ' ', ' '], "🡲":['A', ' ', 'Z'], "🡶":['A', 'B', ' ']}, True, Salida:
def CheckLetras(palabra, listas, cruce: bool):
	direcciones = []
	for key in listas.keys(): # Por cada direccion posible
		#Formo tuplas con las letras de la palabra y las celdas de la trayectorias,
		# luego verifico que la celda este vacia o que sea igual a la letra de la posicion respectiva en la palabra
		ban = all((letra2 == ' ' or (letra1 == letra2 and cruce)) for  letra1, letra2 in zip(palabra, listas[key]))
		if ban:
			direcciones.append(key) 
	return direcciones


#CheckPuntaje: (int, int) -> List[List[int]] -> List[string] -> int -> List(string)
#Toma la coordenada, los puntajes de las celdas de la sopa, las posibles direcciones, 
# el largo de la palabra,
# y devuelve las direcciones ordenadas por el puntaje de la celda donde terminaria la palabra
# dandole prioridad a las direcciones verticales y horizontales
def CheckPuntaje(coord: (int, int), puntajes, direcciones, largo):
	aux = list() 
	aux2 = list()
	largo -= 1
	(x,y) = coord

	#Por cada direccion posible agrego la tupla (dir, pts) en la lista, 
	# pts siendo los puntos de la posicion final de la palabra  
	if "🡳" in direcciones: aux.append(("🡳", puntajes[x+largo][y]   ))
	if "🡲" in direcciones: aux.append(("🡲", puntajes[ x ][y+largo] ))
	if "🡱" in direcciones: aux.append(("🡱", puntajes[x-largo][ y ] ))
	if "🡰" in direcciones: aux.append(("🡰", puntajes[ x ][y-largo] ))
	if "🡶" in direcciones: aux2.append(("🡶", puntajes[x+largo][y+largo] ))
	if "🡷" in direcciones: aux2.append(("🡷", puntajes[x+largo][y-largo] ))
	if "🡵" in direcciones: aux2.append(("🡵", puntajes[x-largo][y+largo] ))
	if "🡴" in direcciones: aux2.append(("🡴", puntajes[x-largo][y-largo] ))

	#Ordeno las listas en funcion del puntaje
	aux = sorted(aux, key=config.second, reverse = True)
	aux2 = sorted(aux2, key=config.second, reverse = True)

	#Devuelvo primero las listas horizontales y verticales
	return list(map(config.first, aux)) + list(map(config.first, aux2))


# Filtro las direcciones en funcion de si la palabra entra, las letras con las que se intersecta
#y las ordeno por el puntaje de la celda de la letra final de la palabra en cada direccion
def ChecksMetodico(coord: (int, int), sopa, puntajes, direcciones, palabra, cruce):
	direcciones = CheckEspacio(coord, direcciones, len(sopa[0]), len(palabra))
	listas = listas_a_checkear(coord, sopa, direcciones, len(palabra))
	direcciones = CheckLetras(palabra, listas, cruce)
	direcciones = CheckPuntaje(coord, puntajes, direcciones, len(palabra))
	return direcciones

# Filtro las direcciones en funcion de si la palabra entra, las letras con las que se intersecta
def Checks(coord: (int, int), sopa, direcciones, palabra, cruce):
	direcciones = CheckEspacio(coord, direcciones, len(sopa[0]), len(palabra))
	listas = listas_a_checkear(coord, sopa, direcciones, len(palabra))
	direcciones = CheckLetras(palabra, listas, cruce)
	return direcciones

#ChecksPreliminares: List[string] -> int -> int -> Bool
#Si la cantidad de soma de la cantidad de letras de las palabras es mas grande que la sopa
# o si hay una palabra mas larga que la sopa, devuelvo falso y verdadero de lo contrario
def ChecksPreliminares(palabras, dimension, dificultad):
	ban = True
	letras = sum([len(palabras[i]) for i in range(len(palabras))])
	if(letras > dimension*dimension and dificultad != 3): ban = False

	if len(palabras[0]) > dimension: ban = False

	return ban

#Funcion vieja la dejo por las dudas
#def CheckNoRepetidasViejo(palabras, direcciones, SopaResuelta):
#	(sopa, lista) = SopaResuelta
#	ban = True
#	for (palabra, (coord, palabra2, dir)) in zip(palabras, lista):
#		encontradas = config.buscar(sopa, palabra, direcciones)
#
#		capicua = 2 if palabra == palabra[::-1] else 1
#
#		if len(encontradas) != capicua:
#			sopa2 = [sopa[i].copy() for i in range(len(sopa[0]))]
#			config.borrarPal(sopa2, coord, palabra2, dir)
#			encontradas = config.buscar(sopa2, palabra, direcciones)
#			if len(encontradas) == 0:
#				ban = False
#	return ban

#ChecksPreliminares: List[string] -> List[string] -> (List[List[char]], List[((int, int), string, string)]) -> Bool
#Tomo las lista de palabras, la de las direcciones y la tupla con la sopa y la palabras de la sopa en
# formato (coord, palabra, direccion)
# y devuelvo True si no se forma la misma palabra de otra forma y False de lo contrario
def CheckNoRepetidas(palabras, direcciones, SopaResuelta):
	(sopa, lista) = SopaResuelta
	ban = True
	for palabra in palabras:
		capicua = 2 if palabra == palabra[::-1] else 1 # Me fijo si es palindromo
		veces = 0

		for palabra2 in palabras: # Cuento cuantas veces aparece dentro de otras palabras
			veces = veces + palabra2.count(palabra)

		veces = veces * capicua

		encontradas = config.buscar(sopa, palabra, direcciones)  # cuantas veces aparece en la sopa
		if len(encontradas) > veces: ban = False # si aparece mas veces en la sopa de las que tendria

	return ban 

