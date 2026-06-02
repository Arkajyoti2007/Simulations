import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation 



## Intial conditions
G=6.67e-11
c=3e8  # m/s
m1=1.99e30  # kg
m2=3.3e23 # kg
r1=np.array([0.0,0.0]) # m
r2=np.array([0.0,7e10]) # m
v1=np.array([0.0,0.0])
v2=np.array([39000.0,0.0]) # m/s
dt=10 # s
set_frame_gap=5000

# Acceleration by GTR

def acceleration(m_other , r_sel , r_other , v_self):
    r_rel=r_sel-r_other
    h=np.cross(r_rel,v_self)

    a = np.zeros(2)
    
    a = -((G*m_other)/np.linalg.norm(r_rel)**3)*(1 + (3*np.linalg.norm(h)**2)/(c*c*np.linalg.norm(r_rel)**2))*r_rel
    return a

# Animating part

fig,ax=plt.subplots()
ax.set_xlim(-11e10,11e10)
ax.set_ylim(-11e10,11e10)
ax.set_aspect('equal')
ax.set_title('Mercurys orbital shifting (High precision)')

body1,=ax.plot([],[],'yo',markersize=10)
traj1,=ax.plot([],[],'b-')

body2,=ax.plot([],[],'bo',markersize=5)
traj2,=ax.plot([],[],'b-')

x_list1=[]
y_list1=[]

x_list2=[]
y_list2=[]

a1=acceleration(m2,r1,r2,v1)
a2=acceleration(m1,r2,r1,v2)

def animate(i):
    global r1,r2,v1,v2,dt,a1,a2
    
    for _ in range(set_frame_gap):
        r1=r1 + v1*dt + 0.5*a1*dt**2
        r2=r2 + v2*dt + 0.5*a2*dt**2
        
        a_new1=acceleration(m2,r1,r2,v1)
        a_new2=acceleration(m1,r2,r1,v2)

        v1= v1 + 0.5*(a1 + a_new1)*dt
        v2= v2 + 0.5*(a2 + a_new2)*dt

        a1=a_new1
        a2=a_new2

    x_list1.append(r1[0])
    x_list2.append(r2[0])

    y_list1.append(r1[1])
    y_list2.append(r2[1])

    body1.set_data([r1[0]],[r1[1]])
    traj1.set_data(x_list1,y_list1)

    body2.set_data([r2[0]],[r2[1]])
    traj2.set_data(x_list2,y_list2)

    return body1,traj1,body2,traj2

ani=FuncAnimation(fig=fig,func=animate,frames=1000,interval=5,blit=True)
plt.show()
    

