import time
import numpy as np

N = int(input('Scegli numero di punti: '))
x1 = float(input('estremo inferiore x: '))
x2 = float(input('estremo superiore x: '))
y1 = float(input('estremo inferiore y: '))
y2 = float(input('estremo superiore y: '))

start_time=time.time()
def f(x, y):
    return np.sin(np.pi*x) + np.cos(np.pi*x)

x = np.linspace(x1, x2, 5000)
y = np.linspace(y1, y2, 5000)
M=np.max(f(x, y))
m=np.min(f(x, y))

fig = plt.figure()
ax = fig.gca(projection='3d')

d=0
I=0
if M > 0:
    for i in range(1, N):
        a=np.random.uniform(x1, x2)
        b=np.random.uniform(y1, y2)
        c=np.random.uniform(0, M)
        if c < f(a, b):
            d+=1

    I=d/N * ((x2-x1)*(y2-y1)*M)

D=0
if m < 0:
    for i in range(1, N):
        a=np.random.uniform(x1, x2)
        b=np.random.uniform(y1, y2)
        c=np.random.uniform(m, 0)
        if c > f(a, b):
            D+=1

    I = I + D/N * ((x2-x1)*(y2-y1)*m)


dI = ((x2-x1)*(y2-y1)*(M - m))*np.sqrt((d+D)/N * (1-(d+D)/N))/np.sqrt(N)
print('%f +- %f' %(I, dI))

print("--- %s seconds ---" % (time.time() - start_time))