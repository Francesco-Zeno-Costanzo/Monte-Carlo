import numpy as np
import random as rn
import scipy.integrate as si
import matplotlib.pyplot as plt

#campionamento di una gaussiana
N = 50000             #grandezza del campione
s = 1                 #varianza della distribuzione da campionare
m = 5                 #media della distribuzione da campionare
delta = 0.1           #passo dell'algoritmo
start = 0             #punto di partenza
x=np.array([])        #array del campione
def p(x):
    '''distribuzione da campionare
    '''
    return np.exp(-((x-m)**2)/(2*s))


#array per il plot e nrmalizzazione
t=np.linspace(0, 10, N+1)
Norm=si.simps(p(t), t, dx=1/len(t), even='first' )

#algortimo metropolis
naccept=0
counter=0
q = start
for i in range(N):

    counter += 1
    qp = q + delta*(2*(rn.random())-1)
    w = p(qp)/p(q)
    r = rn.random()

    if w > r:
        q = qp
        naccept+=1

    x = np.insert(x, len(x), q)

print( naccept/counter)#accettanza

#elimino parte del campione per essere sicuro ceh la catena abbia termalizzato
x1=x[10000:]
m1=np.mean(x1)
m2=np.mean(x)
l=np.linspace(0, N, N)

#data blocking pler il calcolo degli errori (i dati sono correlati)
def DB(v, m):
    """
    Funzione che esegure il data blocking
    Parameters
    ----------
    v : array
        contiene i dati di cui calcolare l'errore
    m : float
        media degli elemnti di v

    Return
    ----------
    dx : float
        errore sulla media degli elemti di v
    """
    z=0
    k=6
    for j in range(1,len(v)//(2)**k):
        a=0
        for i in range(1, 2**k + 1):
            a=a+v[(2**k)*(j-1)+i]
            a=a/(2**k)
            a=a-m
            a=a**2
        z=z+a
    dx=np.sqrt(z)*((2**k)/len(v))
    return dx

#calcolo erroe in entrambi i modi per confronto
dm=DB(x, m2)
dm1=DB(x1, m1)
dm2= np.std(x)/np.sqrt(len(x)-1)
dm3= np.std(x1)/np.sqrt(len(x1)-1)


fig1 = plt.figure(1)
plt.suptitle('Algoritmo Metropolis', fontsize=20)
frame1=fig1.add_axes((.05,.55,.4,.35))
plt.title('$\overline{x}=%.2f \pm %.2f (\sigma = %.3f)$'%(m2, dm, dm2), fontsize=20)
plt.grid()
plt.hist(x, 100,  histtype = 'step', density=True)
plt.plot(t, p(t)/Norm)
plt.xlabel('tutte le iterazioni', fontsize=15)

frame2=fig1.add_axes((.55,.55,.4,.35))
plt.title('$\overline{x}=%.2f \pm %.2f  (\sigma = %.3f)$'%(m1, dm1, dm3), fontsize=20)
plt.grid()
plt.hist(x1, 100,  histtype = 'step', density=True)
plt.plot(t, p(t)/Norm)
plt.xlabel('le ultime %d iterazioni' %len(x1), fontsize=15)

#controlliamo la termalizzazione della catena
frame1=fig1.add_axes((.1,.1,.8,.35))
plt.title('Evoluzione della catena', fontsize=15)
plt.xlabel('iterazioni', fontsize=15)
plt.plot(l, x)
plt.grid()
plt.show()
