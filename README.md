# Monte-Carlo
These codes are simple examples of the use of the Monte Carlo method to evaluete integrals; the examples stop to three dimensions but the generalization to high dimensions is simple.
The power of the montecarlo methods lies in the fact that the error always scales as the inverse of the root of N (number of points generated) regardless of the dimensionality.
If instead we were to use a grid in a D-dimensional domain, with N hypercubets with side proportional to the inverse of the D-th root of N

<a href="https://www.codecogs.com/eqnedit.php?latex=\delta\propto\frac{1}{\sqrt[D]{N}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\delta\propto\frac{1}{\sqrt[D]{N}}" title="\delta\propto\frac{1}{\sqrt[D]{N}}" /></a>

a good integration method would produce an error per hypercube proportional to the power D + k-th of the side of the hypercube (where k depends on the method) and for a regular function, the errors add up and therefore we will have N times this error

<a href="https://www.codecogs.com/eqnedit.php?latex=\Delta=N&space;\delta^{D&plus;k}\propto&space;N^{-\frac{k}{D}}" target="_blank"><img src="https://latex.codecogs.com/png.latex?\Delta=N&space;\delta^{D&plus;k}\propto&space;N^{-\frac{k}{D}}" title="\Delta=N \delta^{D+k}\propto N^{-\frac{k}{D}}" /></a>

Per each k there will always be D such that the ratio is less than 1/2 and hence slower than montecarlo.

The Metropolis Algorithm, on the other hand, is a monte carlo method for sampling an unknown distribution starting from one proportional to it.
