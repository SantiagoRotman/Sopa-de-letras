dificultades = {
	1: ["🡳","🡲"],
	2: ["🡳","🡲","🡶"],
	3: ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]
}

archivos = {
	'C_EXE': 'a.out',
	'salidaC': 'out.txt',
	'lemario': 'lemario.txt',
	'entradaC': 'entrada.c'
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

def second(tupla): 
	return tupla[1]