#include <stdio.h>
#include <stdlib.h>
#include<time.h>
#include <math.h>

#define R  1.0
#define N  10000000//00

double VS(int D){
	double v= pow(M_PI, D/2.0) * pow(R, D) / tgamma(1.0 + D/2.0);
	return v;
}

double MC(int D){
	long int c=0;
	double z=0;
	double I=pow(2*R, D);
	double *x;
	x=(double *)calloc(D, sizeof(double));
	for(long int i=0; i<N; i++){
		z=0;
		for(int j=0; j<D; j++){
			x[j]=((double)rand()/RAND_MAX)*(2.0*R)-R;
			z+=(x[j]*x[j]);
		}
		if(z<=R) {
			c++;
		}
	}
	I=I*(c/(N*1.0));
	return I;
}

int main (void){
	srand(time(NULL));
	double l=0;
	double m=0;
	printf("D   MC \t \t esatto \t diff \n");
	for(int D=2; D<19; D++){
		m=l=0;
		l=MC(D);
		m=VS(D);
		printf("%d | %f \t %f \t %f \n", D,  l,m, fabs((l-m)/m));
	}
	return 0;
}
	
