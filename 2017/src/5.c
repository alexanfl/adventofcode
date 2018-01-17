#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void get_column_from_file(FILE *, int [], int);
int jump(int [], int, int);
void perform_jumps(int [], int);
void display_controls(int, int);

int main(int argc, const char *argv[]) {

    if (argc != 3) {
        printf("Error: Requires 2 arguments—data file and number of lines.\n\n");
        abort();
    }

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
    int number_of_jumps = 0;

    printf("Current position is %d with value %d.\n", current_position, jump_offsets[current_position]);

    while (current_position >= 0 && current_position < number_of_lines) {
        current_position = jump(jump_offsets, current_position, number_of_lines);
        number_of_jumps++;
    }
    printf("\nPerformed %d jumps to escape the maze!\n", number_of_jumps);
}

int jump(int jump_offsets[], int current_position, int number_of_lines) {
    int new_position = 0;

    new_position = current_position + jump_offsets[current_position];

    if (jump_offsets[current_position] >= 3) 
        jump_offsets[current_position]--;
    else
        jump_offsets[current_position]++;

    int is_controls = 0;
   
    display_controls(is_controls, new_position); 

    return new_position;
}

void display_controls(int is_controls, int new_position) {
    if (is_controls) {
        printf("Press any button to jump.\n");
        getchar();
        printf("Jumped to position %d\n\n", new_position);
    }
    return;
}
