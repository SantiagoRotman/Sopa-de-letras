import sys
sys.path.append("../")
from src.procedures.core import InsertarPalabra_random, JugarRandom, InsertarPalabra_metodico, JugarMetodico, inicio_juego
from src.config.config import buscar, imprimir_sopa
from src.procedures.checks import CheckNoRepetidas 


sopaV = [
	[' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' '],
	[' ', ' ', ' ', ' ', ' ']
]

puntajes = [
	[5, 4, 3, 4, 5],
	[4, 3, 2, 3, 4],
	[3, 2, 1, 2, 3],
	[4, 3, 2, 3, 4],
	[5, 4, 3, 4, 5]
]

sopaA = [
	['A', 'A', 'A', 'A', 'A',],
	[' ', ' ', ' ', ' ', 'X',],
	[' ', ' ', ' ', ' ', 'X',],
	[' ', ' ', ' ', ' ', 'X',],
	[' ', ' ', ' ', ' ', 'X',]
]
direcciones = [["🡳","🡲"], ["🡳","🡲","🡶"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]]
palabras = ["LEO", "VEIAA", "NETFLIX"]
palabras2 = ["PEPE", "BUSCA", "UN", "LOL"]
palabras3 = ["ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXY"]


def test_InsertarPalabra_random():
	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	InsertarPalabra_random(sopa2, palabras[0], ["🡳"], 0)
	encontradas = buscar(sopa2, palabras[0], ["🡳"]) 

	assert (len(encontradas) == 1) and (("🡳", palabras[0]) == encontradas[0])

	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	InsertarPalabra_random(sopa2, palabras[1], direcciones[1], 0)
	encontradas = buscar(sopa2, palabras[1], direcciones[1]) 

	assert (len(encontradas) == 1) and (palabras[1] == encontradas[0][1]) and (encontradas[0][0] in direcciones[1])

	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	InsertarPalabra_random(sopa2, palabras[1], ["🡶","🡵","🡷","🡴"], 0)
	encontradas = buscar(sopa2, palabras[1], ["🡶","🡵","🡷","🡴"]) 

	assert (len(encontradas) == 1) and (palabras[1] == encontradas[0][1]) and (encontradas[0][0] in ["🡶","🡵","🡷","🡴"])

	sopa2 = [sopaA[i].copy() for i in range(len(sopaA[0]))]
	InsertarPalabra_random(sopa2, "ABBBB", direcciones[2], 1)
	encontradas = buscar(sopa2, "ABBBB", direcciones[2]) 

	assert (len(encontradas) == 1) and ("ABBBB" == encontradas[0][1]) and (encontradas[0][0] in ["🡷","🡳","🡶"])

	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	assert not InsertarPalabra_random(sopa2, palabras[2], direcciones[2], 0)

def test_JugarRandom():
	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	(sopa2, lista) = JugarRandom(sopa2, palabras2, direcciones[2], 1)
	for palabra in palabras2:
		encontradas = buscar(sopa2, palabra, direcciones[2])
		capicua = 2 if palabra == palabra[::-1] else 1
		assert (len(encontradas) == capicua) and (palabra == encontradas[0][1])
	assert len(lista) == len(palabras2)

	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	assert not JugarRandom(sopa2, ["LARGASA"]+palabras2, direcciones[2], 1)
	
def test_JugarMetodico():
	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	(sopa2, lista) = JugarMetodico(sopa2, palabras2, puntajes, direcciones[2], 1)
	for palabra in palabras2:
		encontradas = buscar(sopa2, palabra, direcciones[2])
		capicua = 2 if palabra == palabra[::-1] else 1
		assert (len(encontradas) == capicua) and (palabra == encontradas[0][1])
	assert len(lista) == len(palabras2)

	sopa2 = [sopaV[i].copy() for i in range(len(sopaV[0]))]
	(sopa2, lista) = JugarMetodico(sopa2, palabras3, puntajes, direcciones[2], 1)
	for palabra in palabras3:
		encontradas = buscar(sopa2, palabra, direcciones[2])
		capicua = 2 if palabra == palabra[::-1] else 1
		assert (len(encontradas) == capicua) and (palabra == encontradas[0][1])
	assert len(lista) == len(palabras3)

	assert JugarMetodico(sopa2, palabras3+["XXX"], puntajes, direcciones[2], 1) == False

	(sopa2, lista) = JugarMetodico([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']], ["ABC","AJK","JBX", "ABZ"], [[3,2,3],[2,1,2],[3,2,3]], direcciones[2], 1)
	for palabra in ["ABC","AJK","JBX", "ABZ"]:
		encontradas = buscar(sopa2, palabra, direcciones[2])
		capicua = 2 if palabra == palabra[::-1] else 1
		assert (len(encontradas) == capicua) and (palabra == encontradas[0][1])
	assert len(lista) == len(["ABC","AJK","JBX", "ABZ"])