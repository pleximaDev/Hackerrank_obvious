#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* readline();
char** split_string(char*);

long arrayManipulation(int n, int queries_rows, int queries_columns, int** queries)
{
    // int arr[n] = {0};
    long *arr = malloc(n * sizeof(long));
    // memset(arr, 0, sizeof(*arr));
    memset(arr, 0, n * sizeof(long));
    for(int i = 0; i < queries_rows; i++)
    {
        for(int j = *(*(queries + i) + 0); j <= *(*(queries + i) + 1); j++)
        {
            // printf("from %d to %d\n", *(*(queries + i) + 0), *(*(queries + i) + 1));
            // printf("add %d to arr[%d]\n", *(*(queries + i) + 2), j);
            *(arr + j - 1) += *(*(queries + i) + 2);
        }
        for(int l = 0; l < n; l++)
        {
            printf("arr[%d] = %d\n", l, *(arr + l));
        }
        printf("\n");
    }
    // printf("n == %d\n", n);
    // printf("q_r == %d\n", queries_rows);
    // printf("q_c == %d\n", queries_columns);
    // printf("que == %d\n", *(*(queries + 2) + 0));

    /*
    for(int i = 0; i < n; i++)
    {
        printf("arr[%d] = %d\n", i, arr[i]);
    }
    */
    long max = 0;
    for(int i = 0; i < n; i++)
    {
        if (*(arr + i) > max) max = *(arr + i);
        // printf("arr[%d] = %d\n", i, arr[i]);
    }

    // *(*(queries + 2) + 0)   *(*(queries + rows) + columns)
    return max;
}

int main()
{
    FILE* fptr = fopen(getenv("OUTPUT_PATH"), "w");

    char** nm = split_string(readline());

    char* n_endptr;
    char* n_str = nm[0];
    int n = strtol(n_str, &n_endptr, 10);

    if (n_endptr == n_str || *n_endptr != '\0') { exit(EXIT_FAILURE); }

    char* m_endptr;
    char* m_str = nm[1];
    int m = strtol(m_str, &m_endptr, 10);

    if (m_endptr == m_str || *m_endptr != '\0') { exit(EXIT_FAILURE); }

    int** queries = malloc(m * sizeof(int*));

    for (int i = 0; i < m; i++) {
        *(queries + i) = malloc(3 * (sizeof(int)));

        char** queries_item_temp = split_string(readline());

        for (int j = 0; j < 3; j++) {
            char* queries_item_endptr;
            char* queries_item_str = *(queries_item_temp + j);
            int queries_item = strtol(queries_item_str, &queries_item_endptr, 10);

            if (queries_item_endptr == queries_item_str || *queries_item_endptr != '\0') { exit(EXIT_FAILURE); }

            *(*(queries + i) + j) = queries_item;
        }
    }

    int queries_rows = m;
    int queries_columns = 3;

    long result = arrayManipulation(n, queries_rows, queries_columns, queries);

    fprintf(fptr, "%ld\n", result);

    fclose(fptr);

    return 0;
}

char* readline() {
    size_t alloc_length = 1024;
    size_t data_length = 0;
    char* data = malloc(alloc_length);

    while (true) {
        char* cursor = data + data_length;
        char* line = fgets(cursor, alloc_length - data_length, stdin);

        if (!line) { break; }

        data_length += strlen(cursor);

        if (data_length < alloc_length - 1 || data[data_length - 1] == '\n') { break; }

        size_t new_length = alloc_length << 1;
        data = realloc(data, new_length);

        if (!data) { break; }

        alloc_length = new_length;
    }

    if (data[data_length - 1] == '\n') {
        data[data_length - 1] = '\0';
    }

    data = realloc(data, data_length);

    return data;
}

char** split_string(char* str) {
    char** splits = NULL;
    char* token = strtok(str, " ");

    int spaces = 0;

    while (token) {
        splits = realloc(splits, sizeof(char*) * ++spaces);
        if (!splits) {
            return splits;
        }

        splits[spaces - 1] = token;

        token = strtok(NULL, " ");
    }

    return splits;
}

