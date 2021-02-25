import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2,1,constrained_layout=True)
fig.suptitle("Proyectil con resistencia")

for i in range(10,90,10):
    v0 = 700
    x0 = 0.0
    y0 = 0.0
    t = 0.0 
    dt = 0.05
    g = 9.81
    b2m = 4e-5 
	
    yt, xt = np.array([]), np.array([])
    vt, tt = np.array([]), np.array([])

    v0x = v0*np.cos(i*np.pi/180)
    v0y = v0*np.sin(i*np.pi/180)
	
    while True:
        t += dt
        v = np.sqrt(v0y**2 + v0x**2)
        xi = x0 + v0x*dt
        vix = v0x - b2m*v*v0x*dt
        xt = np.append(xt,xi)
        x0 = xi
        yi = y0 + v0y*dt
        viy = v0y - g*dt - b2m*v*v0y*dt
        yt = np.append(yt,yi)
        y0 = yi
        vt = np.append(vt,v)
        tt = np.append(tt,t)
        v0x = vix
        v0y = viy
        if(y0 < 0.0):
        	break
	
    ax1.plot(xt,yt, label=str(i)+"°")
    ax2.plot(tt,vt, label=str(i)+"°")

ax1.set_ylabel("Altura (m)")
ax1.set_xlabel("Alcance (m)")
ax1.grid()
ax1.legend(bbox_to_anchor = (1.05,1.05))

ax2.set_ylabel("Velocidad (m/s)")
ax2.set_xlabel("Tiempo (s)")
ax2.grid()
ax2.legend(bbox_to_anchor = (1.05,1.05))

plt.show()