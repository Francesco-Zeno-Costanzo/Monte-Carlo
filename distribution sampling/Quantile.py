import numpy as np
import scipy.integrate as si
import matplotlib.pyplot as plt
from scipy.interpolate import InterpolatedUnivariateSpline

#creo la distribuzione da campionare come array come fossero dati sperimentali
x = np.linspace(-1, 1, 50000)
g=1
y = np.sqrt(1-x**2)*np.exp(-g*x)
'''
ne calcolo l'integrale per normalizzarla, la normalizzazione
garantirà di poter utilizzare sempre il generatore uniforme fra 0 e 1
'''
Norm = si.simps(y, x, dx=1/len(x), even='first')
y = y/Norm

#interpolo con polinomi cubici
s3 = InterpolatedUnivariateSpline(x, y, k=3)

#calcolo la funzione cumulativa
cdf = np.array([s3.integral(x[0], i) for i in x])

def prob(x1, x2, cdf):
    '''restituisce la probabilità che una variabile casuale
       sia compresa fra x1 e x2
    '''
    CDF = InterpolatedUnivariateSpline(x, cdf)
    return CDF(x1) - CDF(x2)

print(prob(0.5, -0.5, cdf))

#tolgo possibili valori uguali altrimenti l'interpolazione successiva non funzionerebbe
xq, iq = np.unique(cdf, return_index=True) #faccio ritornare anche l'indice corrispondente

#scabio x con y per invertire la funzione cumulativa e ottenere la funzione quantile
yq = x[iq]
Quantile = InterpolatedUnivariateSpline(xq, yq) #interpolo la funzione quantile
'''
genero un array di numeri casuali uniformemnte distribuuiti fra 0 e 1
applicandoci la funzione quantile otterò una variabile distibuita secondo
la funzione di distribuzione iniziale
'''
Y=Quantile(np.random.uniform(size=len(x)))


plt.figure(1)
plt.grid()
plt.title('Campionamento con funzione quantile')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.plot(x, y, '.', label='distibuzione')
plt.plot(x, s3(x), 'k', label='interpolazione')
plt.hist(Y, 100, histtype='step', density=True)
plt.legend(loc='best')
plt.show()