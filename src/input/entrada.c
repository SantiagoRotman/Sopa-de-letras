#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include<time.h>
#define MAX_WORDS 249950

int arg_check(int argc, char **argv);
//float diagonal(char* lado);
void imprimir(int largo, char* lemario[], char **argv, FILE *out);


int main(int argc, char **argv){
	if (0 == arg_check(argc, argv)) return 1;
	srand(time(0));
	char  buff[255];
    char* lemario[MAX_WORDS];

    int i;
	FILE *in, *out;
    in = fopen(argv[1], "r+");
    out = fopen("out.txt", "w");

	for(i = 0; fscanf(in, "%[^\n] ", buff) != EOF; i++ )
	{
		lemario[i] = malloc(1+strlen(buff)*sizeof(char));
		strcpy(lemario[i], buff);

	}

	imprimir(i, lemario, argv, out);
	
	for(int j = 0; j < i; j++){
		free(lemario[j]);
	}
	fclose(in);
	fclose(out); 

	return 0;
	
}


int arg_check(int argc, char **argv)
{
	if(argc != 5) return 0;
	if(sizeof(argv[1]) != sizeof(char*)) return 0;
	if(!atoi(argv[2]))   return 0;
	if(!atoi(argv[3]))   return 0;
	if(!atoi(argv[4]))   return 0;
	return 1;
}

//float diagonal(char* lado){
//	return sqrt(2*pow(atoi(lado), 2));
//}

void imprimir(int largo, char* lemario[], char **argv, FILE *out)
{
	fprintf(out, "DIMENSION\n");
	fprintf(out, "%s\n", argv[2]);

	fprintf(out, "PALABRAS\n");
	for(int i = 0; i < atoi(argv[3]); i++)
	{
		fprintf(out, "%s\n", lemario[rand()%largo]);
	}

	fprintf(out, "COMPLEJIDAD\n");
	if(atoi(argv[4]) < 0) fprintf(out, "0\n");
	if(atoi(argv[4]) > 3) fprintf(out, "3\n");
	else fprintf(out, "%s\n", argv[4]);
}