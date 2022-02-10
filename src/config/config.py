dificultades = {
	1: ["🡳","🡲"],
	2: ["🡳","🡲","🡶"],
	3: ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]
}

archivos = {
	"C_EXE": "a.out",
	"salidaC": "out.txt",
	"lemario": "lemario.txt",
	"entradaC": "entrada.c"
}

variables = {
	'MAX_INTENTOS': 20
}

info = {
    "name": 'Sopa_de_Letras',
    "version": '1.0.0',
    "author": 'Santiago Rotman'
}

def imprimir_sopa(sopa):
	for linea in sopa:
		print('|', end='')
		for letra in linea:
			if type(letra) is int:
				print(letra, end=' |') if letra < 10 else print(letra, end='|')
			else:
				print(letra, end='|')
		print('')

def first(tupla): 
	return tupla[0]

def second(tupla): 
	return tupla[1]