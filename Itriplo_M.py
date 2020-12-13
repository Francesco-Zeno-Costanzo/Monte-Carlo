import time
import numpy as np

N = int(input('Scegli numero di punti: '))
x1 = float(input('estremo inferiore x: '))
x2 = float(input('estremo superiore x: '))
y1 = float(input('estremo inferiore y: '))
y2 = float(input('estremo superiore y: '))
z1 = float(input('estremo inferiore z: '))
z2 = float(input('estremo superiore z: '))

start_time=time.time()
def f(x, y, z):
    return np.sin(x+y)+np.arctan(z)

x = np.linspace(x1, x2, 5000)
y = np.linspace(y1, y2, 5000)
z = np.linspace(z1, z2, 5000)
M=np.max(f(x, y, z))
m=np.min(f(x, y, z))
e=0
I=0

if M > 0:
    for i in range(1, N):
        a=np.random.uniform(x1, x2)
        b=np.random.uniform(y1, y2)
        c=np.random.uniform(z1, z2)
        d=np.random.uniform(0, M)
        if d < f(a, b, c):
            e+=1

    I=e/N * ((x2-x1)*(y2-y1)*(z2-z1)*M)

E=0
if m < 0:
    for i in range(1, N):
        a=np.random.uniform(x1, x2)
        b=np.random.uniform(y1, y2)
        c=np.random.uniform(z1, z2)
        d=np.random.uniform(m, 0)
        if d > f(a, b, c):
            E+=1

    I = I + E/N * ((x2-x1)*(y2-y1)*(z2-z1)*m)


dI = ((x2-x1)*(y2-y1)*(z2-z1)*(M - m))*np.sqrt((e+E)/N * (1-(e+E)/N))/np.sqrt(N)
print('%f +- %f' %(I, dI))

print("--- %s seconds ---" % (time.time() - start_time))