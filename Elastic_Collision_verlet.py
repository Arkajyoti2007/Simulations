import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def dist(r1,r2):
    return np.linalg.norm(r1-r2)

#Generate points
N=300
dt=0.1
tmax=1000
r=np.zeros((N,2))
v=np.zeros((N,2))
m=np.zeros(N)
c=2
for i in range(N):
    r[i]=[np.random.uniform(-100,100),np.random.uniform(-100,100)]
    v[i]=[np.random.uniform(0,10),np.random.uniform(0,10)]
    m[i]=10

#Elastic collision tracker
def collision(v1,v2,r1,r2,m1,m2):
    d_sq=dist(r1,r2)**2
    
    if d_sq==0:
        return v1,v2
    v1_new= v1 -(2*m2/(m1+m2))*(np.dot(v1-v2,r1-r2)/d_sq)*(r1-r2) 
    v2_new= v2 -(2*m1/(m1+m2))*(np.dot(v2-v1,r2-r1)/d_sq)*(r2-r1)
    return v1_new,v2_new
    


def update_frame(r,v,m):
    v_new=v.copy()
    for i in range(N):
        for j in range(i+1,N):
            if dist(r[i],r[j])<=c:
                r_rel=r[i]-r[j]
                v_rel=v[i]-v[j]

                if np.dot(r_rel,v_rel)<0:
                    v_new[i],v_new[j]=collision(v[i],v[j],r[i],r[j],m[i],m[j])
    
    r_new=r+v_new*dt

    for i in range(N):
        if r_new[i,0]>=100-c or r_new[i,0]<=-100+c:
            v_new[i,0]=-1*v_new[i,0]
            r_new[i,0]=r[i,0]+v_new[i,0]*dt

        if r_new[i,1]>=100-c or r_new[i,1]<=-100+c:
            v_new[i,1]=-1*v_new[i,1]
            r_new[i,1]=r[i,1]+v_new[i,1]*dt
    return r_new , v_new

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

ax1.set_xlim(-100, 100)
ax1.set_ylim(-100, 100)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_title('2D Elastic Collision Simulation')
ax1.set_aspect('equal')
bodies, = ax1.plot([], [], 'ro', ms=4)

ax2.set_xlim(0,25)
ax2.set_ylim(0, N // 2) 
ax2.set_xlabel('Speed (Magnitude of Velocity)')
ax2.set_ylabel('Number of Particles')
ax2.set_title('Velocity Distribution')


bins = np.linspace(0, 25, 20) 
bin_centers = 0.5 * (bins[1:] + bins[:-1]) # Get the middle of each bin to plot a dot/line
speeds = np.linalg.norm(v, axis=1)
counts, _ = np.histogram(speeds, bins=bins)

vel_line, = ax2.plot([], [], 'b-', lw=2, marker='o')

def init():
    bodies.set_data(r[:,0],r[:,1])
    vel_line.set_data(bin_centers, counts)
    return bodies,vel_line

def animate(frame):
    global r,v
    r,v=update_frame(r,v,m)
    bodies.set_data(r[:,0],r[:,1])

    speeds = np.linalg.norm(v, axis=1)
    new_counts, _ = np.histogram(speeds, bins=bins)
    vel_line.set_data(bin_centers, new_counts)

    return bodies,vel_line

ani=FuncAnimation(fig,animate,frames=tmax,interval=20,init_func=init,blit=True)

plt.tight_layout()
plt.show()
