import sys
import itertools
sys.path.append("../")
from src.procedures.checks import listas_a_checkear, CheckEspacio, CheckLetras, CheckPuntaje, ChecksMetodico, CheckNoRepetidas, ChecksPreliminares


dir = [["🡳","🡲"], ["🡳","🡲","🡶"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]]
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
	['A', 'B', 'C', 'D', 'E'],
	['F', 'G', 'H', 'I', 'J'],
	['K', 'L', 'M', 'O', 'P'],
	['Q', 'R', 'S', 'T', 'U'],
	['V', 'W', 'X', 'Y', 'Z']
]
sopaB = [
	[' ', ' ', ' ', 'U', ' '],
	[' ', ' ', ' ', 'N', ' '],
	['P', 'E', 'L', 'A', 'S'],
	[' ', ' ', ' ', ' ', ' '],
	[' ', 'L', 'E', 'S', ' ']
]
sopaC = [
	[' ', ' ', ' ', 'U', ' '],
	[' ', ' ', ' ', 'N', ' '],
	[' ', ' ', ' ', 'A', ' '],
	[' ', ' ', ' ', ' ', ' '],
	['U', 'N', 'A', 'S', 'I']
]
sopaD = [
	[' ', ' ', ' ', 'U', ' '],
	['L', ' ', ' ', 'N', ' '],
	['A', ' ', ' ', 'A', ' '],
	['N', ' ', ' ', ' ', ' '],
	['U', 'N', 'A', 'S', 'I']
]
sopaE = [
	[' ', ' ', ' ', 'L', ' '],
	['A', ' ', ' ', 'O', ' '],
	['L', ' ', ' ', 'L', ' '],
	['O', ' ', ' ', ' ', ' '],
	['L', 'O', 'L', 'E', 'S']
]
def test_CheckEspacio():
	assert CheckEspacio((0,0), dir[2], 5, 5) == ["🡳","🡲","🡶"]
	assert CheckEspacio((0,4), dir[2], 5, 5) == ["🡳","🡷","🡰"]
	assert CheckEspacio((4,0), dir[2], 5, 5) == ["🡲","🡵","🡱"]
	assert CheckEspacio((4,4), dir[2], 5, 5) == ["🡱","🡰","🡴"]

	assert CheckEspacio((0,2), dir[2], 5, 5) == ["🡳"]
	assert CheckEspacio((0,2), dir[2], 5, 3) == ["🡳","🡲","🡶","🡷","🡰"]
	assert CheckEspacio((4,2), dir[2], 5, 3) == ["🡲","🡵","🡱","🡰","🡴"]
	assert CheckEspacio((2,0), dir[2], 5, 3) == ["🡳","🡲","🡶","🡵","🡱"]
	assert CheckEspacio((2,4), dir[2], 5, 3) == ["🡳","🡱","🡷","🡰","🡴"]

	assert CheckEspacio((2,2), dir[2], 5, 3) == ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"]
	assert CheckEspacio((0,3), dir[2], 5, 3) == ["🡳","🡷","🡰"]
	assert CheckEspacio((2,1), dir[2], 5, 3) == ["🡳","🡲","🡶","🡵","🡱"]


def test_listas_a_checkear():
	listas = listas_a_checkear((0,0), sopaA, ["🡳","🡲","🡶"], 5)
	assert listas == {"🡳":['A', 'F', 'K', 'Q', 'V'], "🡲":['A', 'B', 'C', 'D', 'E'], "🡶":['A', 'G', 'M', 'T', 'Z']} 

	listas = listas_a_checkear((2,2), sopaA, ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], 3)
	assert listas == {"🡳":['M','S','X'], "🡲":['M','O','P'], "🡶":['M','T','Z'], "🡵":['M','I','E'], "🡱":['M','H','C'], "🡷":['M','R','V'], "🡰":['M','L','K'], "🡴":['M','G','A']}


def test_CheckLetras():
	direcciones = CheckLetras("AFKQV", {"🡳":['A', 'F', 'K', 'Q', 'V'], "🡲":['A', 'B', 'C', 'D', 'E'], "🡶":['A', 'G', 'M', 'T', 'Z']}, 1)
	assert direcciones == ["🡳"]

	direcciones = CheckLetras("AFKQV", {"🡳":[' ', 'F', 'K', ' ', ' '], "🡲":[' ', ' ', ' ', 'D', ' '], "🡶":[' ', ' ', ' ', ' ', ' ']}, 1)
	assert direcciones == ["🡳", "🡶"]

	direcciones = CheckLetras("AFKQV", {"🡳":[' ', 'F', 'K', ' ', ' '], "🡲":[' ', ' ', ' ', 'D', ' '], "🡶":[' ', ' ', ' ', ' ', ' ']}, 0)
	assert direcciones == ["🡶"]

	direcciones = CheckLetras("ABB", {"🡳":['A', ' ', ' '], "🡲":['A', ' ', 'Z'], "🡶":['A', 'B', ' ']}, True)
	assert direcciones == ["🡳", "🡶"]



def test_CheckPuntaje():
	direcciones = CheckPuntaje((0,0), puntajes,  ["🡳","🡲","🡶"], 3)
	assert direcciones == ["🡳","🡲","🡶"] or direcciones == ["🡲","🡳","🡶"] 

	direcciones = CheckPuntaje((0,2), puntajes,  ["🡳","🡲","🡶","🡷","🡰"], 3)
	permutations = list(itertools.permutations(["🡳","🡲","🡶","🡷","🡰"]))
	assert tuple(direcciones) in permutations


def test_ChecksPreliminares():
	assert ChecksPreliminares(["AAA","BBB","CCC"], 3, 2)
	assert not ChecksPreliminares(["AAAA","BBB","CCC"], 3, 2)
	assert ChecksPreliminares(["AAA","BBB","CCC", "ABC"], 3, 3)
	assert not ChecksPreliminares(["AAAA","BBB","CCC", "AAB"], 3, 3)


def test_CheckNoRepetidas():
	assert CheckNoRepetidas(["UNA","PELAS", "LES"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaB, [((0,3), "UNA", "🡳"), ((2,0), "PELAS", "🡲"), ((4,1), "LES", "🡲")]))
	assert CheckNoRepetidas(["UNASI","UNA"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaC, [((0,3), "UNA", "🡳"), ((4,0), "UNASI", "🡲")]))
	assert not CheckNoRepetidas(["UNASI","UNA", "NAL"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaD, [((0,3), "UNA", "🡳"), ((4,0), "UNASI", "🡲"), ((3,0), "NAL", "🡱")]))
	assert not CheckNoRepetidas(["LOLES","OLA", "LOL"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaE, [((4,0), "LOLES", "🡲"), ((0,3), "LOL", "🡳"), ((3,0), "OLA", "🡱")]))


	#assert CheckNoRepetidas2(["UNA","PELAS", "LES"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaB, [((0,3), "UNA", "🡳"), ((2,0), "PELAS", "🡲"), ((4,1), "LES", "🡲")]))
	#assert CheckNoRepetidas2(["UNASI","UNA"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaC, [((0,3), "UNA", "🡳"), ((4,0), "UNASI", "🡲")]))
	#assert not CheckNoRepetidas2(["UNASI","UNA", "NAL"], ["🡳","🡲","🡶","🡵","🡱","🡷","🡰","🡴"], (sopaD, [((0,3), "UNA", "🡳"), ((4,0), "UNASI", "🡲"), ((3,0), "NAL", "🡱")]))
