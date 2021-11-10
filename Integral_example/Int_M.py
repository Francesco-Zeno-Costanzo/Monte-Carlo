import time
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

N = int(input('Scegli numero di punti: '))
x1 = float(input('estremo inferiore x: '))
x2 = float(input('estremo superiore x: '))

start_time=time.time()

def f(x):
    return np.sqrt(x)-1
x=np.linspace(x1, x2, 10000)

M=np.max(f(x))
m=np.min(f(x))
I=0
c=0

if M > 0:
    for i in range(1, N):
        a=np.random.uniform(x1, x2)
        b=np.random.uniform(0, M)
        if b < f(a):
            plt.errorbar(a, b, fmt='.', markersize=1, color='red')
            c+=1
        else:
            plt.errorbar(a, b, fmt='.', markersize=1, color='green')

    I=c/N * ((x2-x1)*M)

d=0
if m < 0:
    plt.plot(x, 0*x,color='blue', lw=1)
    for i in range(1, N):
        a=np.random.uniform(x1,x2)
        b=np.random.uniform(m, 0)
        if b > f(a):
            plt.errorbar(a, b, fmt='.', markersize=1, color='red')
            d+=1
        else:
            plt.errorbar(a, b, fmt='.', markersize=1, color='green')
    I = I + d/N * ((x2-x1)*m)


dI = ((x2-x1)*(M - m))*np.sqrt((c+d)/N * (1-(c+d)/N))/np.sqrt(N)
print('%f +- %f' %(I, dI))

H = lambda x: f(x)
a, da=integrate.quad(H, x1, x2)
print('%.15f +- %.15f' %(a, da))
print(abs((I-a)/a))


plt.figure(1)
plt.title('I $\simeq$ %f $\pm$ %f; N=%.0e' %(I, dI, N), fontsize=15)
plt.ylabel('$f(x)= \sqrt{x} - 1$', fontsize=15)
plt.xlabel('I = %.15f $\pm$ %.15f' %(a, da), fontsize=15)


plt.plot(x, f(x),color='blue', lw=1)
plt.xlim(x1,x2)
plt.ylim(m, M)
plt.show()
print("--- %s seconds ---" % (time.time() - start_time))