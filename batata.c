#include <stdio.h>
#include <string.h>

int main() {
    int D;
    char N[20]; // suficiente para N < 10^8

    while (1) {
        scanf("%d %s", &D, N);

        // condição de parada
        if (D == 0 && strcmp(N, "0") == 0) {
            break;
        }

        char d_char = D + '0';
        char resultado[20];
        int j = 0;

        // remove o dígito defeituoso
        for (int i = 0; N[i] != '\0'; i++) {
            if (N[i] != d_char) {
                resultado[j++] = N[i];
            }
        }

        resultado[j] = '\0';

        // se ficou vazio, o valor é 0
        if (j == 0) {
            printf("0\n");
            continue;
        }

        // remove zeros à esquerda
        int k = 0;
        while (resultado[k] == '0' && resultado[k + 1] != '\0') {
            k++;
        }

        printf("%s\n", &resultado[k]);
    }

    return 0;
}