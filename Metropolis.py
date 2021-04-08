import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
N=50000
'''
a=16807,M=(2**31)-1
'''
def GEN(r0,n=1, a=1607,c=0,M=(2**11)-1):
    if n==1:
        return np.mod(a*r0+c,M)/M
    else:
        r=np.zeros(n)
        r[0]=r0
        for i in range(1,n):
            r[i]=np.mod(a*r[i-1]+c,M)
    return r/M

#confronto con i primi 50 momenti della distibuzione uniforme
for i in range(1, 50):
    print(sum(GEN(i, N)**i)/N - 1/(i+1))

##Metropolis
def p(x):
    return 2*np.exp(-(x-5)**2)


delta=6
x=np.array([0.])
N=1000
naccept=0
counter=0
t=np.linspace(0, 10, N+1)
Norm=si.simps(p(t), t, dx=1/len(t), even='first' )

while naccept < N:
    counter+=1
    xt=x[-1]+delta*(2*GEN(counter)-1)
    w=p(xt)/p(x[-1])
    r=GEN(naccept)
    if w > r:
        x=np.insert(x, len(x), xt)
        naccept+=1
#è consigliabile che tale rapporto sia <= 0.5
print( naccept/counter) 

l=np.linspace(0, N, N+1)
plt.figure(1)
plt.title('Metropolis')
plt.grid()
plt.hist(x, 100,  histtype = 'step', density=True)
plt.plot(t, p(t)/Norm)

#controlliamo la termalizzazione della catena
plt.figure(2)
plt.title('Evoluzione della catena')
plt.xlabel('iterazioni')
plt.plot(l, x)
plt.grid()
plt.show()
