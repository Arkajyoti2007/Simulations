import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

N=int(input("Enter no. of bodies (N) : "))

w=2
A=1
dt=0.05

fig,ax=plt.subplots()
ax.set_xlim(-A*1.5,A*1.5)
ax.set_ylim(-A*1.5,A*1.5)

body,=ax.plot([],[],'ro',ms=8)

def animate(frame):
    t=frame*dt
    x=[]
    y=[]
    for i in range(N):
        a=np.pi*i/N
        X= A*np.cos(w*t -  a)*np.cos(a)
        Y= A*np.cos(w*t -  a)*np.sin(a)
        x.append(X)
        y.append(Y)
    x.append(x[0])
    y.append(y[0])
    body.set_data(x[:-1],y[:-1])
    return body,

ani=FuncAnimation(fig,animate,frames=200,interval=60,blit=True)



plt.show()
