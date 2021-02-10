import time
import numpy as np
import matplotlib.pyplot as plt

N = int(input('Scegli numero di punti: '))
start_time=time.time()

x=np.linspace(0,1, 10000)
def f(x):
    return np.sqrt(1-x**2)
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
dPi = np.sqrt(c/N * (1-c/N))/np.sqrt(N)
print('%f +- %f' %(Pi, dPi))
print(np.pi)
print(abs((Pi-np.pi)/np.pi))

plt.figure(1)
plt.title('Pi $\simeq$ %f $\pm$ %f ; N=%.0e' %(Pi, dPi, N), fontsize=20)
plt.xlim(0,1)
plt.ylim(0,1)
plt.plot(x, f(x),color='blue', lw=1)
plt.show()

print("--- %s seconds ---" % (time.time() - start_time))
