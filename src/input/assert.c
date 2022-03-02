#include <stdio.h>
#include <string.h>
#include <time.h>
#include "funciones.c"
#include <assert.h>


int main(){
	FILE *input = fopen("testLemario.txt", "r");
	srand(time(0));

	char** lemario = malloc(sizeof(char*) * MAX_WORDS);
	int largo = 0;

	lemario = leerLemario(input, lemario, &largo);

	assert(largo == 6);
	assert(0 == strcmp(lemario[0], "hola"));
	assert(0 == strcmp(lemario[1], "que"));
	assert(0 == strcmp(lemario[2], "tal"));
	assert(0 == strcmp(lemario[3], "pepe"));
	assert(0 == strcmp(lemario[4], "como"));
	assert(0 == strcmp(lemario[5], "estas"));


	
	int usadas[5], usadas2[0], i, pos;
	for (i=0;i<3;i++) usadas[i]=i;

	pos = buscarPal(largo, lemario, usadas2, 0);
	assert(0 <= pos && pos <= 5);

	pos = buscarPal(largo, lemario, usadas, 3);
	assert(3<=pos && pos<=5);


	printf("Tests exitosos\n");

}
