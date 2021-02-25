import numpy as np
import matplotlib.pyplot as plt

N_0 = 100.0
tau = 1.0
dt = 0.05
x = np.array([])
yi = np.array([])

Nt = N_0
for i in np.arange(0,6,dt):
    x = np.append(x,i)
    yi = np.append(yi,Nt)
    N = Nt - (Nt/tau)*dt
    Nt = N

fig, ax = plt.subplots()
ax.plot(x,yi,label='Aproximación',color='r',marker='.')
ax.plot(x,N_0*np.exp(-x/tau),label='Solución Analítica')

ax.set(xlabel='time (a)', ylabel='N',title='Decaimiento')
ax.grid()
ax.legend()

plt.show()