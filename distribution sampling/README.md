# distribution sampling
These are examples of distribution sampling codes.
metrogauss.py use metropolisi algoritm to sample a normal distribution.

The Metropolis Algorithm, is a Monte Carlo method for sampling an unknown distribution starting from one proportional to it, p(x).
We have to generate a sequence of draws x0, . . . xN , starting from a given x0. We generate xx uniformly in the interval [xk - d, xk + d];
if the probability ratio between the new variable and the old one is greater than a randomly generated number in [0, 1] the move is accepted, otherwise rejected.

<a href="https://www.codecogs.com/eqnedit.php?latex=\\&space;xx&space;\in&space;[x_k&space;-&space;\delta,&space;x_k&space;&plus;&space;\delta&space;]\\&space;r&space;\in&space;[0,&space;1]\\&space;\frac{p(xx)}{p(x_k)}&space;<&space;r&space;\rightarrow&space;x_{k&plus;1}=xx\\&space;\frac{p(xx)}{p(x_k)}&space;>&space;r&space;\rightarrow&space;x_{k&plus;1}=x_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\\&space;xx&space;\in&space;[x_k&space;-&space;\delta,&space;x_k&space;&plus;&space;\delta&space;]\\&space;r&space;\in&space;[0,&space;1]\\&space;\frac{p(xx)}{p(x_k)}&space;<&space;r&space;\rightarrow&space;x_{k&plus;1}=xx\\&space;\frac{p(xx)}{p(x_k)}&space;>&space;r&space;\rightarrow&space;x_{k&plus;1}=x_k" title="\\ xx \in [x_k - \delta, x_k + \delta ]\\ r \in [0, 1]\\ \frac{p(xx)}{p(x_k)} < r \rightarrow x_{k+1}=xx\\ \frac{p(xx)}{p(x_k)} > r \rightarrow x_{k+1}=x_k" /></a>


Quantile.py use the function quantile or percet point function to semple a distribution:
We have a probability density function p(x)>=0. Now let define:

<a href="https://www.codecogs.com/eqnedit.php?latex=F(x)=\int_{-\infty}^x&space;p(t)&space;dt" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F(x)=\int_{-\infty}^x&space;p(t)&space;dt" title="F(x)=\int_{-\infty}^x p(t) dt" /></a>

That is the cumulative function, now if we manage to reverse the cumulativ function we obtein the quantile function <a href="https://www.codecogs.com/eqnedit.php?latex=F^{-1}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F^{-1}" title="F^{-1}" /></a>. 
If q is a random variable ditribuited uniformly in [0, 1] then x define as x = <a href="https://www.codecogs.com/eqnedit.php?latex=F^{-1}(q)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?F^{-1}(q)" title="F^{-1}(q)" /></a> is distribuited according p(x).
