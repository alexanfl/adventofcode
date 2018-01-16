#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define NO_OF_CHARS 26

/*
 * Compile:
 * > gcc -o 4 4.c
 * Run:
 * > ./4 <datafile>
 * 
 * Data file must consist of rows of space separated words.
 * 
 * The program can check if a word appears twice in a sentence,
 * or if a word is an anagram of another word in the sentence.
*/


int evaluate_passphrase(char *);
int get_number_of_valid_passphrases(FILE *, char **, int);
int check_passphrase_without_anagrams(char **, int *);
int check_passphrase_with_anagrams(char **, int *);
void get_list_of_words(char *, int *, char **);
void update_number_of_words(int *);
void display_result(int, int);
int is_anagram(char*, char*);

int main(int argc, const char *argv[])
{
    char *list_of_words[50];
    char *mode = "r";
    char filename[25];
    strcpy(filename, argv[1]);

    FILE *ifp;

    // Set to 0 to check only for repeated words, 1 to check anagrams too.
    int anagrams = 1;

    // Open file and store content
    ifp = fopen(filename, mode);

    // Function that checks each line of the file for repeated words and anagrams. 
    get_number_of_valid_passphrases(ifp, list_of_words, anagrams);

    fclose(ifp);

    return 0;
}


int get_number_of_valid_passphrases(FILE *ifp, char *list_of_words[], int anagrams) {
    /*
     * Function that returns the number of lines that has no repeated and/or
     * anagrams.
    */
    char line[128];
    int number_of_invalid_passphrases = 0;
    int number_of_valid_passphrases = 0;
    int number_of_passphrases = 0;
    int i, j;

    while (fgets(line, sizeof(line), ifp)) {
        int number_of_words = 0;
        int *number_of_words_ptr = &number_of_words;

        char *passphrase;
        passphrase = strtok(line, " ");

        get_list_of_words(passphrase, number_of_words_ptr, list_of_words);

        if (anagrams)
            number_of_invalid_passphrases += check_passphrase_with_anagrams(
                    list_of_words, number_of_words_ptr);
        else
            number_of_invalid_passphrases += check_passphrase_without_anagrams(
                    list_of_words, number_of_words_ptr);

        number_of_passphrases += 1;
    }

    number_of_valid_passphrases = number_of_passphrases - number_of_invalid_passphrases;

    display_result(number_of_passphrases, number_of_valid_passphrases);

    return number_of_valid_passphrases;

}

void display_result(int number_of_passphrases, int number_of_valid_passphrases) {
    printf("The number of total passphrases is %d.\n", number_of_passphrases);
    printf("The number of valid passphrases is %d.\n", number_of_valid_passphrases);
}

int is_anagram(char *str1, char *str2) {
    /*
     * Checks if two strings are anagrams.
     *
     * Each time a character appears, we increment the counter of the character
     * if it is in the first string and subtract if it is in the second string. 
     *
     * If one character counter is different from zero at the end, we know that 
     * the strings are not anagrams.
    */

    // Initiate a count array of zeros.
    int count[NO_OF_CHARS] = {0};
    int i;

    // Words that are of different length can't be anagrams.
    if (strlen(str1) != strlen(str2)) return 0;
 
    for (i = 0; str1[i] && str2[i];  i++) {
        count[str1[i]-'a']++;
        count[str2[i]-'a']--;
    }
 
    for (i = 0; i < NO_OF_CHARS; i++)
        if (count[i]) return 0;

    return 1;
}


void get_list_of_words(char *passphrase, int *number_of_words_ptr, 
         char *list_of_words[]) {
    while (passphrase != NULL) {
        list_of_words[*number_of_words_ptr] = passphrase;
        passphrase = strtok (NULL, " \n");
        update_number_of_words(number_of_words_ptr);
    }
}

void update_number_of_words(int *number_of_words_ptr) {
    *number_of_words_ptr += 1;
}

int check_passphrase_without_anagrams(char *list_of_words[], int *number_of_words_ptr) {
    int number_of_violations = 0;
    int i, j;
    for (i = 0; i < *number_of_words_ptr; i++) {
        for (j = i+1; j < *number_of_words_ptr; j++) {
            if (!strcmp(list_of_words[i], list_of_words[j])) {
                number_of_violations += 1;
            }
        }
    }
    if (number_of_violations) return 1;

    return 0;
}


int check_passphrase_with_anagrams(char *list_of_words[], int *number_of_words_ptr) {
    int number_of_violations = 0;
    int i, j;
    for (i = 0; i < *number_of_words_ptr; i++) {
        for (j = i+1; j < *number_of_words_ptr; j++) {
            if (!strcmp(list_of_words[i], list_of_words[j]) 
                    || is_anagram(list_of_words[i], list_of_words[j])) {
                number_of_violations += 1;
            }
        }
    }
    if (number_of_violations) return 1;
    else return 0;
}
