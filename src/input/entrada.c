#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>
#include "funciones.c"
#define MAX_WORDS 20000 // Largo del array inicial y del incremento


int main(int argc, char **argv){
	if (0 == arg_check(argc, argv)) return 1; // Si los argumentos no son validos termina el programa
	srand(time(0));

    char** lemario = malloc(sizeof(char*) * MAX_WORDS); // Pide memoria para el lemario

	FILE *in, *out; 
    in = fopen(argv[1], "r+"); // Abro el lemario pasado por argumento
    out = fopen("out.txt", "w"); // Abro o creo el archivo de salida

    int largo;
	lemario = (char**)leerLemario(in, lemario, &largo);

	// Imprimo al archivo de salida los argumentos y las palabras del lemario
	//verificando que no esten repetidas y no sean una sola letra
	imprimir(largo, lemario, argv, out); 
	
	// Libero la memoria 
	for(int j = 0; j < largo; j++){
		free(lemario[j]);
	}
	free(lemario);

	// Cierro los archivos
	fclose(in);
	fclose(out); 

	return 0;
	
}


