import random as rn
import scipy.integrate as si
import matplotlib.pyplot as plt
def p(x):
    return 2*np.exp(-(x)**2)+np.exp(-(x+3)**2)+np.exp(-(x-3)**2)


delta=5
x=np.array([0.])
N=5000
naccept=0
counter=0
t=np.linspace(-5, 5, N+1)
Norm=si.simps(p(t), t, dx=1/len(t), even='first' )

while naccept < N:
    counter+=1
    xt=x[-1]+delta*(2*rn.random()-1)
    w=p(xt)/p(x[-1])
    r=rn.random()
    if w > r:
        x=np.insert(x, len(x), xt)
        naccept+=1

print( naccept/counter)
plt.title('Metropolis')
plt.grid()
plt.hist(x, 100,  histtype = 'step', density=True)
plt.plot(t, p(t)/Norm)
plt.show()
