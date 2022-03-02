#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include<time.h>
#define MAX_WORDS 20000 // Largo del array inicial y del incremento

//arg_check: int -> char** -> int 
//Los parametros representan la cantidad de argumentos y los argumentos respectivamente
// se retorna 1 si la cantidad de argumentos y su tipo es correcto, de lo contrario 0
int arg_check(int argc, char **argv);

char** leerLemario(FILE *in, char* lemario[], int* largoFinal);

//imprimir: int -> char*[] -> char** -> FILE -> void
//Los parmaetros representan el largo del lemario, el lemario, los argumentos del programa,
// y el puntero al archivo de salida.
// no se retorna nada ya que imprime al archivo de salida
void imprimir(int largo, char* lemario[], char **argv, FILE *out);

//buscarPal: int -> char*[] -> int[] -> int -> int
//Los parmaetros representan el largo del lemario, el lemario, la lista de las posiciones
// de las palabras seleccionadas y la cantidad de palabras ya ingresadas-
// devuelve la posicion de una nueva palabra no repetida y de largo mayor que 1
int buscarPal(int largo, char* lemario[], int palabras[], int ingresadas);



int arg_check(int argc, char **argv)
{
	if(argc != 5) return 0; 						// Chequeo la cantidad de argumentos
	if(sizeof(argv[1]) != sizeof(char*)) return 0;  // El segundo argumento tiene que ser el lemario
	if(!atoi(argv[2]))   return 0;					// El tercero tiene que ser un numero 
	if(!atoi(argv[3]))   return 0;					// El cuarto tiene que ser un numero
	if(!atoi(argv[4]))   return 0;					// El quinto tiene que ser un numero
	return 1;
}

char** leerLemario(FILE *in, char* lemario[], int* largoFinal){
	char buff[255];
	int i;
    int largo = MAX_WORDS;
	for(i = 0; fscanf(in, "%[^\n] ", buff) != EOF; i++ ) // Recorro el lemario linea por linea 
	{
		if(i == largo){// Si se termino el espacio alocado pido mas
			largo = largo + MAX_WORDS;
			lemario = (char**) realloc(lemario, sizeof(char*) * largo);
		}
		lemario[i] = malloc(1+strlen(buff)*sizeof(char));  // Pido memoria para la palabra
		strcpy(lemario[i], buff); 
	}
	*largoFinal = i;
	return lemario;

}

int buscarPal(int largo, char* lemario[], int palabras[], int ingresadas){
	int pos, ban = 1;
	while(ban){ // Busco una palabra no repetida y de largo mayor a 1
		ban = 0;
		pos = rand()%largo;

		if(strlen(lemario[pos]) == 2) // Largo distinto de 1
			ban = 1;

		for(int j = 0; j < ingresadas && !ban; j++){ // Y que no este repetida
			if(lemario[pos] == lemario[palabras[j]]) 
				ban = 1;
		}
	}
	return pos;
}

void imprimir(int largo, char* lemario[], char **argv, FILE *out)
{
	fprintf(out, "DIMENSION\n");
	fprintf(out, "%s\n", argv[2]);
	fprintf(out, "PALABRAS\n");

	int palabras[atoi(argv[3])];
	for(int i = 0; i < atoi(argv[3]); i++) // Cantidad de palabras
	{
		int pos = buscarPal(largo, lemario, palabras, i);
		palabras[i] = pos; 					 // Agrego a la lista de palabras la posision de la nueva palabra 
		fprintf(out, "%s\n", lemario[pos]);  // Imprimo la palabra al archivo de salida
	}

	fprintf(out, "COMPLEJIDAD\n");
	if(atoi(argv[4]) < 0) fprintf(out, "0\n");
	if(atoi(argv[4]) > 3) fprintf(out, "3\n");
	else fprintf(out, "%s\n", argv[4]);
}