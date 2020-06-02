// Author : Koshvendra Singh
// Date   : 01/06/2020
//Description : exponential distributed (mean=0.5) random numbers using transformation method in c

// Compile using   gcc transformation.c -lm -o trans.out
//NOTE : exponential distribution is plotted in python by using  the file created here

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(void)
{
  int num=10000;
  double *x,*y;
  x=(double*) malloc(sizeof(double) * num);
  y=(double*) malloc(sizeof(double) * num);

  //creating random number and it's transformation
  for (int i=0;i < num;i++){
    
    x[i]=(double)rand()/(double)RAND_MAX;
    y[i]=-2* log(x[i]);
  }
  //printing these random number and transformation in a txt file
  FILE *file;
  int st =remove("transformation.txt");
  file=fopen("transformation.txt","w+");

  for (int i=0;i<num;i++){
    fprintf(file,"%f    %f\n",x[i],y[i]);
      }

  return(0);
    
}
