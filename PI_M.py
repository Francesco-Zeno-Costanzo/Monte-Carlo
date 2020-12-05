import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,1, 10000)
def f(x):
    return np.sqrt(1-x**2)

N = input('Scegli numero di punti: ')
N = int(N)
c=0

for i in range(1,N):
    a=np.random.rand()
    b=np.random.rand()
    r=a**2 + b**2
    if r< 1:
        plt.errorbar(a, b, fmt='.', markersize=1, color='red')
        c+=1
    else:
        plt.errorbar(a, b, fmt='.', markersize=1,  color='green')

Pi=4*c/N
print(Pi)
print(np.pi)
print(np.pi)

plt.figure(1)
plt.title('Pi $\simeq$ %f, N=%.0e' %(Pi, N), fontsize=20)
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x, f(x),color='blue', lw=1)
plt.show()
