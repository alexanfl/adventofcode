#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void get_column_from_file(FILE *, int [], int);
int jump(int [], int, int);
void perform_jumps(int [], int);

int main(int argc, const char *argv[]) {
    char *mode = "r";
    char filename[25];
    strcpy(filename, argv[1]);

    FILE *ifp;

    int number_of_lines = atoi(argv[2]);
    int jump_offsets[number_of_lines];

    // Open file and store content
    ifp = fopen(filename, mode);

    // Store jump offsets in array
    get_column_from_file(ifp, jump_offsets, number_of_lines);
    perform_jumps(jump_offsets, number_of_lines);

    fclose(ifp);
    return 0;
}

void get_column_from_file(FILE *ifp, int array[], int number_of_lines) {
    int i;
    for (i = 0; i < number_of_lines; i++) {
        fscanf(ifp, "%d", &array[i]);
        printf("%d\n", array[i]);
    }
}

void perform_jumps(int jump_offsets[], int number_of_lines) {
    int current_position = 0;
    printf("Current position is %d with value %d.\n", current_position, jump_offsets[current_position]);
    while (current_position >= 0 && current_position < number_of_lines) {
        current_position = jump(jump_offsets, current_position, number_of_lines);
    }
}

int jump(int jump_offsets[], int current_position, int number_of_lines) {
    int new_position = 0;
    new_position = current_position + jump_offsets[current_position];
    jump_offsets[current_position] += 1;
    printf("Press any button to jump.\n");
    getchar();
    printf("Jumped to position %d\n\n", new_position);
    return new_position;
}
