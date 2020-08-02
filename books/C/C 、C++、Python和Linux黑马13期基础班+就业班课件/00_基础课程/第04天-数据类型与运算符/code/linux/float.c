#include <stdio.h>

int main()
{
	float a = 3.14;
	printf("%f\n", a);
	printf("%lu, %lu, %lu\n", sizeof(float), sizeof(double), sizeof(long double));
	printf("%d\n", a);
	int b = 10;
	printf("%f\n", b);
	double a1 = 3;
	int a2 = 2;
	double a3 = a1 / a2;
	//int tmp = a1 / a2;
	//double a3 = tmp;
	printf("%lf\n", a3);
	return 0;
}

