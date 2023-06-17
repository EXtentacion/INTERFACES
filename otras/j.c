//crea dos funciones y mandalas llamar dentro del main



// Path: k.c




#include <stdio.h>
#include <stdlib.h>

int suma(int a, int b);
int resta(int a, int b);

int main()
{
    int a, b, c, d;
    printf("Dame el valor de a: ");
    scanf("%d", &a);
    printf("Dame el valor de b: ");
    scanf("%d", &b);
    c = suma(a, b);
    d = resta(a, b);
    printf("La suma es: %d\n", c);
    printf("La resta es: %d\n", d);
    return 0;
}

int suma(int a, int b)
{
    int c;
    c = a + b;
    return c;
}

int resta(int a, int b)
{
    int c;
    c = a - b;
    return c;
}


//como hago para ejecutar el programa desde la terminal?

//gcc -o nombre_del_ejecutable nombre_del_archivo.c

//./nombre_del_ejecutable