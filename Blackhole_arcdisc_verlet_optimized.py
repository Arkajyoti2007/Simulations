import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Ellipse # Added to draw the oval
import time

#Initial conditons
G=1
dt=0.01
tmax=3000
N_bodies=500
r_in=50
r_out=100
M_bh=20000
m_bodies=0.001
N=N_bodies+1
i,j = np.triu_indices(N,k=1)

#Generate points
r=np.zeros((N,2))
v=np.zeros((N,2))
m=np.zeros(N)
m[0]=M_bh
r[0]=[0.0,0.0]
v[0]=[0.0,0.0]
for K in range(N_bodies):
    k= K+1
    m[k]=m_bodies
    dist=np.random.uniform(r_in,r_out)
    theta=np.random.uniform(0,2*np.pi)
    r[k,0]=dist*np.cos(theta)
    r[k,1]=dist*np.sin(theta)
    V=np.sqrt(G*m[0]/dist)
    v[k,0]=-V*r[k,1]/dist
    v[k,1]=V*r[k,0]/dist

def acceleration(m, r):
    e = 0.1
    a_x = np.zeros(N)
    a_y = np.zeros(N)

    dx = r[j,0] - r[i,0]
    dy = r[j,1] - r[i,1]
    
    dist_sq = dx**2 + dy**2 + e**2
    
    f = (G) / (dist_sq**1.5)

    a_x = np.bincount(i,weights=f*m[j]*dx,minlength=N) - np.bincount(j,weights=f*m[i]*dx,minlength=N)
    a_y = np.bincount(i,weights=f*m[j]*dy,minlength=N) - np.bincount(j,weights=f*m[i]*dy,minlength=N)
    
    return np.column_stack((a_x, a_y))

def verlet(r,v,dt,m,a):
    r_new=r.copy()
    r_new=r + v*dt + 0.5*a*dt**2
    a_new=acceleration(m,r_new)
    v=v+0.5*(a+a_new)*dt
    r=r_new
    return r , v, a_new

fig,ax=plt.subplots(figsize=(7, 7))
ax.set_xlim(-150,150)
ax.set_ylim(-150,150)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Black hole acretion disc')

body=[]
bh_patch = Ellipse((0, 0), width=35, height=15, color='black', zorder=10)
ax.add_patch(bh_patch)
body.append(bh_patch)
for _ in range(N_bodies):
    body.append(ax.plot([],[],'bo',ms=2)[0])

def animate(frame):
    global r,v,a_new
    a=a_new
    r,v,a_new=verlet(r,v,dt,m,a)
    body[0].center = (r[0, 0], r[0, 1])
    for i in range(1,N):
        body[i].set_data([r[i,0]],[r[i,1]])
    return body

a_new = acceleration(m,r)
ani=FuncAnimation(fig,animate,frames=tmax,interval=2,blit=True)
plt.show()


