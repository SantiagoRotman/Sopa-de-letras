#include <stdio.h>
#include <string.h>

int arg_check(int argc, char **argv);

int main(int argc, char **argv){
	FILE* fp;
	char buff[255];
	arg_check(argc, argv);

	fp = fopen(argv[1], "r");

	for(int i = 0; fscanf(fp, "%[^\n] ", buff) != EOF; i++ ){
		printf("%s\n", buff);
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