#include <stdio.h>
#include <stdlib.h>
#define RANDOM_NUMBERS_FILE ("/dev/random")
#define UPPER_BOUND (126)
#define LOWER_BOUND (33)


void GeneratePassword(char* memory, int length){
	FILE* file = fopen(RANDOM_NUMBERS_FILE, "r");
	if(file == NULL){
		printf("File opening error!\n");
		exit(-1);
	}
	int currentChar = fgetc(file);
	if(currentChar == EOF){
		printf("%s could not be read!\n", RANDOM_NUMBERS_FILE);
		exit(-1);
	}
	for(int index = 0; index < length; ++index){
		*(memory + index) = (currentChar % (UPPER_BOUND - LOWER_BOUND)) + LOWER_BOUND;
		currentChar = fgetc(file);
	}
	fclose(file);
}

int main(int argc, char* argv[]){
	if(argc != 2){
		printf("You need to enter the password length!\n");
		return 0;
	}
	int passwordLength = atoi(argv[1]);
	if(passwordLength <= 0){
		printf("You need to enter only positive length!\n");
		return 0;
	}
	printf("Generating a password...\n");
	char* password = (char*)malloc(sizeof(char) * passwordLength);
	GeneratePassword(password, passwordLength);
	printf("Generated password:\n%s\n", password);
	free(password);
	return 0;
}

