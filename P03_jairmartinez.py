import numpy as np
import matplotlib.pyplot as plt

g = 9.81
dt = np.array([1.5,1.0,0.5,0.2]) #Diferente tamaño de paso
v_0 = 0.0

for j in dt:
    t = np.array([])
    v = np.array([])
    vt = v_0
    for i in np.arange(0,10,j):
        t = np.append(t,i)
        v = np.append(v,vt)
        v_f = vt + -g*j
        vt = v_f
    plt.plot(t,v_0 + -g*t,label='Solución Analítica')
    plt.plot(t,v,'r--',label='Aproximación dt = '+str(j))
    plt.xlabel=('time (s)')
    plt.ylabel('velocity (m)')
    plt.title('Movimiento 2')
    plt.grid()
    plt.legend()
    plt.show()