#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include<time.h>

#define L 1000000
#define N 1000000000

double max(double *a) {
	double massimo=a[0];
	for (long int i=0; i<L; i++){
		if(a[i]>massimo){
			massimo=a[i];
		}
	}
	return massimo;
}

double min(double *a) {
	double minimo=a[0];
	for (long int i=0; i<L; i++){
		if(a[i]<minimo){
			minimo=a[i];
		}
	}
	return minimo;
}

double F(double x){
	return sin(x);
}

long double MC(double x1, double x2, double M, double m){
	long int c=0;
	long int d=0;
	double x, y;
	long double I=0;
	if (M > 0){
		for(long int i=0; i<N; i++){
			x=((double)rand()/RAND_MAX)*(x2-x1) + x1;
			y=((double)rand()/RAND_MAX)*(M);
			if(y<F(x)) {
				c++;
			}
		}
		I=((c/(N*1.0)) * ((x2-x1)*M));
	}
	if (m < 0){
		for(long int j=0; j<N; j++){
			x=((double)rand()/RAND_MAX)*(x2-x1) + x1;
			y=((double)rand()/RAND_MAX)*(m);
			if(y>F(x)){
				d++;
			}
		}
		I = I + ((d/(N*1.0)) * ((x2-x1)*m));
	}
	return I;
}
int main (void){
	clock_t start = clock();
	srand(time(NULL));
	double x1, x2, M, m;
	long double I=0;
	printf("primo estremo:");
	scanf("%lf",&x1);
	printf("secondo estremo:");
	scanf("%lf",&x2);
	double a[L];
	for(long int j=0; j<L; j++){
		a[j]=F(x1 + j*((x2 - x1)/(L*1.0)));
	}
	M=max(a);
	m=min(a);
	I=MC(x1, x2, M, m);
	printf("I= %Lf \n", I);
	clock_t end = clock();
	printf("Tempo di esecuzione =  %f secondi \n", ((double)(end - start)) / CLOCKS_PER_SEC);
	return 0;
}
