
def listas_a_checkear(coord: (int, int), sopa, direcciones, largo: int):
	listas = dict()
	aux = []
	(x, y) = coord

	if "🡳" in direcciones:
		for i in range(largo):
			aux.append(sopa[x+i][y])
		listas["🡳"] = aux

	if "🡲" in direcciones:
		for i in range(largo):
			aux.append(sopa[x][y+i])
		listas["🡲"] = aux

	if "🡶" in direcciones:
		for i in range(largo):
			aux.append(sopa[x+i][y+i])
		listas["🡶"] = aux

	if "🡵" in direcciones:
		for i in range(largo):
			aux.append(sopa[x-i][y+i])
		listas["🡵"] = aux

	if "🡱" in direcciones:
		for i in range(largo):
			aux.append(sopa[x-i][y])
		listas["🡱"] = aux

	if "🡷" in direcciones:
		for i in range(largo):
			aux.append(sopa[x+i][y-i])
		listas["🡷"] = aux

	if "🡰" in direcciones:
		for i in range(largo):
			aux.append(sopa[x][y-i])
		listas["🡰"] = aux

	if "🡴" in direcciones:
		for i in range(largo):
			aux.append(sopa[x-i][y-i])
		listas["🡴"] = aux

	return listas


def CheckeEspacio(coord: (int, int)):
	pass
def CheckLetras(coord: (int, int)):
	pass
def Checks(coord: (int, int)):
	pass

#🡱-🡵-🡲-🡶-🡳-🡷-🡰-🡴
def inicio_juego(sopa, palabras: list, dificultad: int):

	if dificultad == 0:
		dir = ["🡳","🡲"] 
	if dificultad == 1:
		dir = ["🡳","🡲","🡶"]  
	else:
		dir = ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]

	palabras = sorted(palabras, key=len, reverse = True)

	print(listas_a_checkear((0,0), sopa, dir, 5))	