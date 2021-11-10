import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


N = int(input('Scegli numero di punti: '))
R = float(input('Scegli il raggio: '))

start_time=time.time()
fig = plt.figure()
ax = fig.gca(projection='3d')
d=0


for i in range(1, N):
    a=np.random.uniform(-R,R)
    b=np.random.uniform(-R,R)
    c=np.random.uniform(-R,R)
    r=np.sqrt(a**2 + b**2 + c**2)
    if r < R:
        #ax.scatter(a, b, c, marker='.', c='red')
        d+=1
    #else:
     #   ax.scatter(a, b, c, marker='.', c='green')


V=((2*R)**3)*d/N
dV=((2*R)**3)*np.sqrt(d/N * (1-d/N))/np.sqrt(N)

V1=4/3 * np.pi * R**3
print('%f +- %f' %(V, dV))
print(V1)
print((V-V1)/V1)


#plt.title('V $\simeq$ %f $\pm$ %f \n V = %f; , N=%.0e' %( V, dV, V1, N), fontsize=20)
#plt.show()
print("--- %s seconds ---" % (time.time() - start_time))