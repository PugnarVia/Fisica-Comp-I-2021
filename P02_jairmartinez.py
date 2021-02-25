import numpy as np
import matplotlib.pyplot as plt

v = 40
dt = 0.05
x_0 = 0.0
t = np.array([])
x = np.array([])

xt = x_0
for i in np.arange(0,10,dt):
    t = np.append(t,i)
    x = np.append(x,xt)
    x_f = xt + v*dt
    xt = x_f

fig, ax = plt.subplots()
ax.plot(t,x,label='Aproximación',color='r',marker='.')
ax.plot(t,x_0 + v*t,label='Solución Analítica')

ax.set(xlabel='time (s)', ylabel='distnace (m)',title='Movimiento')
ax.grid()
ax.legend()

plt.show()