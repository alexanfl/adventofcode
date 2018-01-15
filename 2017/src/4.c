#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int evaluate_passphrase(char *);
void scan_file(FILE *);

int main(int argc, const char *argv[])
{
    char filename[25];
    strcpy(filename, argv[1]);

    evaluate_passphrase(filename);

    return 0;
}

int evaluate_passphrase(char *filename) {
    FILE *ifp;
    char *mode = "r";

    ifp = fopen(filename, mode);
    
    scan_file(ifp);

    return 0;
}

void scan_file(FILE *ifp) {
    char line[128];
    int number_of_invalid_passphrases = 0;
    int number_of_passphrases = 0;
    int i, j;

    while (fgets(line, sizeof(line), ifp)) {
        int number_of_words = 0;
        char *passphrase;
        const char *list_of_words[50];
        int number_of_invalid_passphrases_this_iter = 0;
        /* printf("%s\n", line); */
        passphrase = strtok(line, " ");

        while (passphrase != NULL) {
            list_of_words[number_of_words] = passphrase;
            passphrase = strtok (NULL, " \n");
            number_of_words += 1;
        }
        number_of_passphrases += 1;

        for (i = 0; i < number_of_words; i++) {
            for (j = i+1; j < number_of_words; j++) {
                printf("comparing: %s and %s\n", list_of_words[i], list_of_words[j]);
                printf("\tstrcmp result: %d\n", strcmp(list_of_words[i], list_of_words[j]));
                if (!strcmp(list_of_words[i], list_of_words[j])) {
                    number_of_invalid_passphrases_this_iter += 1;
                    printf("\t\t… and they're equal!\n");
                }
            }
        }
        printf("\n\n");
        if (number_of_invalid_passphrases_this_iter) number_of_invalid_passphrases += 1;
    }

    printf("The number of total passphrases is %d.\n", number_of_passphrases);
    printf("The number of valid passphrases is %d.\n", number_of_passphrases - number_of_invalid_passphrases);
    fclose(ifp);
}
