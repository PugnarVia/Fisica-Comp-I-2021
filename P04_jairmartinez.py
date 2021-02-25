import numpy as np
import matplotlib.pyplot as plt

a = 10
b = 1
vt = 0.0
v_f = 1.0
dt = 0.05
v = np.array([])
t = np.array([])

v_0 = vt
for i in np.arange(0,10,dt):
    v_f = v_0 + (a-b*v_0)*dt
    v_0 = v_f
    v = np.append(v,v_0)
    t = np.append(t,i)

plt.plot(t,(a/b)*(1-np.exp(-b*t)),label='Solución Analítica')
plt.plot(t,v,'r--',label='Aproximación dt = '+str(dt))
plt.xlabel=('time (s)')
plt.ylabel('velocity (m/s)')
plt.title('Movimiento con fricción')
plt.grid()
plt.legend()
plt.show()