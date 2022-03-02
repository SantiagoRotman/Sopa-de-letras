import procedures.checks as checks

dificultades = {
	1: ["🡳","🡲"],
	2: ["🡳","🡲","🡶"],
	3: ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]
}

archivos = {
	"C_Linux":   "a.out",
	"C_Windows": "a.exe",
	"salidaC":   "out.txt",
	"lemario":   "lemario.txt",
	"entradaC":  "entrada.c"
}

variables = {
	'MAX_INTENTOS': 20
}

info = {
    "name": 'Sopa_de_Letras',
    "version": '1.0.0',
    "author": 'Santiago Rotman'
}

#imprimir_sopa: List[List[char]] -> void
def imprimir_sopa(sopa):
	for linea in sopa:
		print('|', end='')
		for letra in linea:
			if type(letra) is int:
				print(letra, end=' |') if letra < 10 else print(letra, end='|')
			else:
				print(letra, end='|')
		print('')


#borrarPal: List[List[char]] -> string -> List[string] -> List[(string, string)]
#Toma la sopa, la palabra y las posibles direcciones de la palabra,
# devuelve las palabras encontradas (si es palindromo devuelve las dos posibilidades)
def buscar(sopa, palabra, dirs):
	dimension = len(sopa[0])
	encontradas = list()
	largo = len(palabra)

	for y in range(dimension):
		for x in range(dimension):
			dirs2 = checks.CheckEspacio((y,x), dirs, dimension, largo)
			listas = checks.listas_a_checkear((y, x), sopa, dirs2, largo)
			listas = [(key, ''.join(listas[key])) for key in listas.keys() if ''.join(listas[key]) == palabra ]

			for (key, pal) in listas:
				encontradas.append((key, pal))
				
	return encontradas


#borrarPal: List[List[char]] -> (int, int) -> string -> string -> List[List[char]]
#Toma la sopa, la coordenada de la palabra, la palabra y la direccion de la palabra,
# devuelve la sopa sin la palabra
def borrarPal(sopa, coord, palabra, dir): # al final no se usa 
	largo  = len(palabra)

	for i in range(largo):
		sopa[coord[0]][coord[1]] = ' '
		coord = mover(coord, dir)

#mover: (int, int) -> string -> (int, int)
#Los argumentos representan la coordenada y la direccion en que nos queremos mover
# devuelve la coordenada de la siguiente celda en funcion de la direccion 
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


def first(tupla): 
	return tupla[0]

def second(tupla): 
	return tupla[1]