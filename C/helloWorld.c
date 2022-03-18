#include <stdio.h>

void main() {

    printf("Let us calculate the area of the circle\n");

    float pi = 3.14159;
    float r;
    float area;

    printf("Enter radius : ");
    scanf("%f",&r);

    area = pi * r * r;
    printf("The area of the circle is %f",&area);
    printf("\n");

}