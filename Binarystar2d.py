import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


N=2
m=np.array([10.0,10.0]) # kg
r=np.array([[4.0,96.0],[4.0,100.0]],float) # m
v=np.array([[-1.054,-0.556],[1.054,-0.556]],float) # m/s^2
G=1
dt=0.1
tmax=10000

def acceleration(m,r):
    e=0.1
    a=np.zeros_like(r)
    for i in range(N):
        for j in range(N):
            if i!=j:
                a[i]+=(G*m[j]/(np.linalg.norm(r[i]-r[j])**2 + e**2)**1.5)*(r[j]-r[i])
    return a

def verlet(r,v,dt,m,a):
    r_new=r.copy()
    r_new=r + v*dt + 0.5*a*dt**2
    a_new=acceleration(m,r_new)
    v=v+0.5*(a+a_new)*dt
    r=r_new
    return r , v

fig,ax=plt.subplots(figsize=(7, 7))
ax.set_xlim(-100,100)
ax.set_ylim(-100,100)
ax.grid(True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Binary star simulation')
ax.set_aspect('equal')


colors = ["#01034fff", "#620505ff"]
body=[ax.plot([],[],'o',color=colors[i],ms=5,zorder=3)[0] for i in range(N)]
trails=[ax.plot([],[],'-',color=colors[i],alpha=0.5,zorder=2)[0] for i in range(N)]


x_history=np.zeros((N,tmax))
y_history=np.zeros((N,tmax))

def init():
    for i in range(N):
        body[i].set_data([r[i, 0]], [r[i, 1]])
        trails[i].set_data([], [])
    return body + trails

def animate(frame):
    global r,v
    a=acceleration(m,r)
    r,v=verlet(r,v,dt,m,a)
    for i in range(N):
        x_history[i,frame]=r[i,0]
        y_history[i,frame]=r[i,1]
        body[i].set_data([x_history[i,frame]],[y_history[i,frame]])
        trails[i].set_data([x_history[i,:frame]],[y_history[i,:frame]])
    return body+trails
 
ani=FuncAnimation(fig,animate,frames=tmax,interval=1,init_func=init,blit=False)

plt.show()

