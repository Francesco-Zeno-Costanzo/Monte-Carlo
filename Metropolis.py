import numpy as np
import random as rn
import scipy.integrate as si
import matplotlib.pyplot as plt
N=50000
'''
a=16807,M=(2**31)-1
'''
M=(2**31)-1
def GEN(r0,n=1, a=16807,c=0):
    if n==1:
        return np.mod(a*r0+c,M)
    else:
        r=np.zeros(n)
        r[0]=r0
        for i in range(1,n):
            r[i]=np.mod(a*r[i-1]+c,M)
    return r

#confronto con i primi 50 momenti della distibuzione uniforme
for i in range(1, 50):
    print(sum((GEN(i, N)/M)**i)/N - 1/(i+1))

##Metropolis
def p(x):
    return np.exp(-((x-5)**2)/2)


delta=0.1
x=np.array([0.])
N=15000
naccept=0
counter=0
t=np.linspace(0, 10, N+1)
Norm=si.simps(p(t), t, dx=1/len(t), even='first' )

while naccept < N:
    counter+=1
    xt=x[-1]+delta*(2*(rn.random())-1)
    w=p(xt)/p(x[-1])
    r=rn.random()
    if w > r:
        x=np.insert(x, len(x), xt)
        naccept+=1
print( naccept/counter)

x1=x[5000:]
m1=np.mean(x1)
m=np.mean(x)
l=np.linspace(0, N, N+1)

def err(v, m):
    a=0
    z=0
    k=6
    for j in range(1,len(v)//(2)**k):
        for i in range(1, 2**k + 1):
            a=a+v[(2**k)*(j-1)+i]
            a=a/(2**k)
            a=a-m
            a=a**2
        z=z+a
    dx=z*((2**k)/len(x1))**2
    return dx

dx=err(x, m)
dx1=err(x1, m1)

fig1 = plt.figure(1)
plt.suptitle('Algoritmo Metropolis', fontsize=20)
frame1=fig1.add_axes((.05,.55,.4,.35))
plt.title('$\overline{x}=%.2f \pm %.2f$'%(m, dx), fontsize=20)
plt.grid()
plt.hist(x, 100,  histtype = 'step', density=True)
plt.plot(t, p(t))
plt.xlabel('tutte le iterazioni', fontsize=15)

frame2=fig1.add_axes((.55,.55,.4,.35))
plt.title('$\overline{x}=%.2f \pm %.2f$'%(m1, dx1), fontsize=20)
plt.grid()
plt.hist(x1, 100,  histtype = 'step', density=True)
plt.plot(t, p(t))
plt.xlabel('le ultime 10000 iterazioni', fontsize=15)

#controlliamo la termalizzazione della catena
frame1=fig1.add_axes((.1,.1,.8,.35))
plt.title('Evoluzione della catena', fontsize=15)
plt.xlabel('iterazioni', fontsize=15)
plt.plot(l, x)
plt.grid()
plt.show()
