# Monte-Carlo
These codes are simple examples of the use of the Monte Carlo method to evaluete integrals; we stop with three dimensional examples but the generalization to higher dimensions is simple.
intmon.c is the equivalent of Int_M.py.
Vsfera.c compute the N-dimensional hypersphere volume.
The power of the montecarlo methods is that the error always scales as the inverse of the root of N (number of points generated) regardless of the dimensionality.
If we were to use a grid in a D-dimensional domain, with N hypercubets with side proportional to the inverse of the D-th root of N

<a href="https://www.codecogs.com/eqnedit.php?latex=\delta\propto\frac{1}{\sqrt[D]{N}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\delta\propto\frac{1}{\sqrt[D]{N}}" title="\delta\propto\frac{1}{\sqrt[D]{N}}" /></a>

a good integration method instead we would produce an error per hypercube proportional to the power D + k-th of the side of the hypercube (where k depends on the method) and for a regular function, the errors add up and therefore we will have N times this error

<a href="https://www.codecogs.com/eqnedit.php?latex=\Delta=N&space;\delta^{D&plus;k}\propto&space;N^{-\frac{k}{D}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\Delta=N&space;\delta^{D&plus;k}\propto&space;N^{-\frac{k}{D}}" title="\Delta=N \delta^{D+k}\propto N^{-\frac{k}{D}}" /></a>

Per each k there will always be D such that the ratio is less than 1/2 and hence slower than montecarlo.

The Metropolis Algorithm, on the other hand, is a monte carlo method for sampling an unknown distribution starting from one proportional to it, p(x).
We have to generate a sequence of extractions x0, . . . xN , starting from a given x0. We generate xx uniformly in the interval [xk - d, xk + d];
if the probability ratio between the new variable and the old one is greater than a randomly generated number in [0, 1] the move is accepted, otherwise rejected.

<a href="https://www.codecogs.com/eqnedit.php?latex=\\&space;xx&space;\in&space;[x_k&space;-&space;\delta,&space;x_k&space;&plus;&space;\delta&space;]\\&space;r&space;\in&space;[0,&space;1]\\&space;\frac{p(xx)}{p(x_k)}&space;<&space;r&space;\rightarrow&space;x_{k&plus;1}=xx\\&space;\frac{p(xx)}{p(x_k)}&space;>&space;r&space;\rightarrow&space;x_{k&plus;1}=x_k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\\&space;xx&space;\in&space;[x_k&space;-&space;\delta,&space;x_k&space;&plus;&space;\delta&space;]\\&space;r&space;\in&space;[0,&space;1]\\&space;\frac{p(xx)}{p(x_k)}&space;<&space;r&space;\rightarrow&space;x_{k&plus;1}=xx\\&space;\frac{p(xx)}{p(x_k)}&space;>&space;r&space;\rightarrow&space;x_{k&plus;1}=x_k" title="\\ xx \in [x_k - \delta, x_k + \delta ]\\ r \in [0, 1]\\ \frac{p(xx)}{p(x_k)} < r \rightarrow x_{k+1}=xx\\ \frac{p(xx)}{p(x_k)} > r \rightarrow x_{k+1}=x_k" /></a>

To test the goodness of the generator we compare the moments of the uniform distribution:

<a href="https://www.codecogs.com/eqnedit.php?latex=\int_0&space;^1&space;x^p&space;dx&space;=&space;\frac{1}{1&plus;p}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\int_0&space;^1&space;x^p&space;dx&space;=&space;\frac{1}{1&plus;p}" title="\int_0 ^1 x^p dx = \frac{1}{1+p}" /></a>
