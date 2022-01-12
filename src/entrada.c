#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#define MAX_WORDS 1000000
#define PATH "/home/santi/escuela/Sopa-de-letras/docs/lemario.txt" //temporal

int arg_check(int argc, char **argv);
float diagonal(char* lado);


int main(int argc, char **argv){
	arg_check(argc, argv);
	char  buff[255];
    char* lemario[MAX_WORDS];

	FILE *in, *out;
    in = fopen(PATH, "r+");
    out = fopen("out.txt", "w");

	for(int i = 0; fscanf(in, "%[^\n] ", buff) != EOF; i++ ){
		if(strlen(buff)-1 <= diagonal(argv[2])){
			lemario[i] = malloc(1+strlen(buff)*sizeof(char));
			strcpy(lemario[i], buff);
			printf("%s\n", lemario[i]);
		}
		else i--;
	}
}


int arg_check(int argc, char **argv){
	if(argc != 5) return 0;
	if(sizeof(argv[1]) != sizeof(char*)) return 0;
	if(sizeof(argv[2]) != sizeof(int))   return 0;
	if(sizeof(argv[3]) != sizeof(int))   return 0;
	if(sizeof(argv[4]) != sizeof(int))   return 0;
	return 1;
}

float diagonal(char* lado){
	return sqrt(2*pow(atoi(lado), 2));
}