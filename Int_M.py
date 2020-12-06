import time
import numpy as np
import random as rd
from scipy import integrate
import matplotlib.pyplot as plt

def f(x):
    return np.sin(np.pi*x)**2

N = int(input('Scegli numero di punti: '))
a1 = float(input('estremo inferiore: '))
b1 = float(input('estremo superiore: '))
x=np.linspace(a1, b1, 10000)

start_time=time.time()

M=np.max(f(x))
m=np.min(f(x))
I=0
c=0
if M > 0:
    for i in range(1,N):
        a=rd.uniform(a1, b1)
        b=rd.uniform(0, M)
        if b < f(a):
            plt.errorbar(a, b, fmt='.', markersize=1, color='red')
            c+=1
        else:
            plt.errorbar(a, b, fmt='.', markersize=1, color='green')

    I=c/N * ((b1-a1)*M)

d=0
if m < 0:
    plt.plot(x, 0*x,color='blue', lw=1)
    for i in range(1,N):
        a=rd.uniform(a1,b1)
        b=rd.uniform(m, 0)
        if b > f(a):
            plt.errorbar(a, b, fmt='.', markersize=1, color='red')
            d+=1
        else:
            plt.errorbar(a, b, fmt='.', markersize=1, color='green')
    I = I + d/N * ((b1-a1)*m)


dI = ((b1-a1)*(M - m))*np.sqrt((c+d)/N * (1-(c+d)/N))/np.sqrt(N)
print('%f +- %f' %(I, dI))

H = lambda x: f(x)
a, da=integrate.quad(H, a1, b1)
print('%.15f +- %.15f' %(a, da))
print(abs((I-a)/a))


plt.figure(1)
plt.title('I $\simeq$ %f $\pm$ %f; N=%.0e' %(I, dI, N), fontsize=15)
plt.ylabel('$f(x)=sin( \pi x)^2$', fontsize=15)
plt.xlabel('I = %.15f $\pm$ %.15f' %(a, da), fontsize=15)


plt.plot(x, f(x),color='blue', lw=1)
plt.xlim(a1,b1)
plt.ylim(np.min(f(x)),np.max(f(x)))
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))