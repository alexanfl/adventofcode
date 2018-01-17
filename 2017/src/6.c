#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void redistribute_block(int **, int, int);
int evaluate_block(int **, int, int);
void find_max_block(int **, int, int, int *, int *);
void update_banks(int **, int, int, int, int);

int main(int argc, const char *argv[]) {
    char *mode = "r";
    char filename[25];
    strcpy(filename, argv[1]);

    FILE *ifp;

    // Open file and store content
    ifp = fopen(filename, mode);

    int size_of_blocks = atoi(argv[2]);
    int N = 100000;
    int number_of_blocks = 1;
   
    // Allocate matric block
    int **block = (int **)malloc(N * sizeof(int *));
    int i;
    for (i=0; i < N; i++)
         block[i] = (int *)malloc(size_of_blocks * sizeof(int));

    int j;
    for (j = 0; j < size_of_blocks; j++) {
        fscanf(ifp, "%d", &block[0][j]);
        block[1][j] = block[0][j];

    }

    while (!evaluate_block(block, size_of_blocks, number_of_blocks - 1)) {
        for (j = 0; j < size_of_blocks; j++) {
            block[number_of_blocks][j] = block[number_of_blocks - 1][j];
        }
        int j;
        redistribute_block(block, size_of_blocks, number_of_blocks);
        number_of_blocks++;
    }

    fclose(ifp);

    return 0;
}

void find_max_block(int **block, int size_of_blocks, int number_of_blocks, 
        int *max_block, int *max_elem) {
    int j;
    for (j = 0; j < size_of_blocks; j++) {
        if (block[number_of_blocks][j] > *max_block) {
            *max_block = block[number_of_blocks][j];
            *max_elem = j;
        }
    }
    return;
}

void redistribute_block(int **block, int size_of_blocks, int number_of_blocks) {

    int max_block = 0;
    int max_elem = 0;
    find_max_block(block, size_of_blocks, number_of_blocks, &max_block, &max_elem);

    // Redistribute the bank with the maximal value of the block.
    block[number_of_blocks][max_elem] = 0;

    // Iterate over banks, increment each until max_block redistributed.
    update_banks(block, size_of_blocks, number_of_blocks, max_block, max_elem);
}

void update_banks(int **block, int size_of_blocks, int number_of_blocks,
            int max_block, int max_elem) {
    int offset;
    int round_counter = 0;
    int j = 0;
    for (offset = max_elem + 1; offset <= max_block + max_elem; offset++) {
        if (offset >= size_of_blocks) {
            if ( !( offset%size_of_blocks ) ) 
                round_counter++;

            j = offset - round_counter*size_of_blocks;
        }
        else j = offset;

        block[number_of_blocks][j]++;
    }

}

int evaluate_block(int **block, int size_of_blocks, int number_of_blocks) {
    int i, j;
    for (i = 0; i < number_of_blocks; i++) {
        int counter = 0;
        for (j = 0; j < size_of_blocks; j++) {
            if (block[number_of_blocks][j] == block[i][j]) {
                counter++;
            }
            if (counter == size_of_blocks) {
                printf("Success! Number of blocks = %d", number_of_blocks);
                return 1;
            }
        }
    }
    return 0;
}
