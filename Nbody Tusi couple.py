import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

w=2
A=1
tmax=50
t=np.linspace(0,tmax,500)

n=9
j1,j2,j3,j4,j5,j6,j7,j8,j9=1,2,3,4,5,6,7,8,9

x1=A*np.cos(w*t -np.pi*j1/n)*np.cos(np.pi*j1/n)
y1=A*np.cos(w*t -np.pi*j1/n)*np.sin(np.pi*j1/n)

x2=A*np.cos(w*t -np.pi*j2/n)*np.cos(np.pi*j2/n)
y2=A*np.cos(w*t -np.pi*j2/n)*np.sin(np.pi*j2/n)

x3=A*np.cos(w*t -np.pi*j3/n)*np.cos(np.pi*j3/n)
y3=A*np.cos(w*t -np.pi*j3/n)*np.sin(np.pi*j3/n)

x4=A*np.cos(w*t -np.pi*j4/n)*np.cos(np.pi*j4/n)
y4=A*np.cos(w*t -np.pi*j4/n)*np.sin(np.pi*j4/n)

x5=A*np.cos(w*t -np.pi*j5/n)*np.cos(np.pi*j5/n)
y5=A*np.cos(w*t -np.pi*j5/n)*np.sin(np.pi*j5/n)

x6=A*np.cos(w*t -np.pi*j6/n)*np.cos(np.pi*j6/n)
y6=A*np.cos(w*t -np.pi*j6/n)*np.sin(np.pi*j6/n)

x7=A*np.cos(w*t -np.pi*j7/n)*np.cos(np.pi*j7/n)
y7=A*np.cos(w*t -np.pi*j7/n)*np.sin(np.pi*j7/n)

x8=A*np.cos(w*t -np.pi*j8/n)*np.cos(np.pi*j8/n)
y8=A*np.cos(w*t -np.pi*j8/n)*np.sin(np.pi*j8/n)

x9=A*np.cos(w*t -np.pi*j9/n)*np.cos(np.pi*j9/n)
y9=A*np.cos(w*t -np.pi*j9/n)*np.sin(np.pi*j9/n)





fig,ax=plt.subplots()
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)


body1,=ax.plot([],[],'ro',markersize=10)
body2,=ax.plot([],[],'ro',markersize=10)
body3,=ax.plot([],[],'ro',markersize=10)
body4,=ax.plot([],[],'ro',markersize=10)
body5,=ax.plot([],[],'ro',markersize=10)
body6,=ax.plot([],[],'ro',markersize=10)
body7,=ax.plot([],[],'ro',markersize=10)
body8,=ax.plot([],[],'ro',markersize=10)
body9,=ax.plot([],[],'ro',markersize=10)
traj,=ax.plot([],[],'b-')




def init():
    body1.set_data([],[])
    body2.set_data([],[])
    body3.set_data([],[])
    body4.set_data([],[])
    body5.set_data([],[])
    body6.set_data([],[])
    body7.set_data([],[])
    body8.set_data([],[])
    body9.set_data([],[])
    traj.set_data([],[])
    return body1,body2,body3,body4,body5,body6,body7,body8,body9,traj

def animate(i):
    body1.set_data([x1[i]],[y1[i]])
    body2.set_data([x2[i]],[y2[i]])
    body3.set_data([x3[i]],[y3[i]])
    body4.set_data([x4[i]],[y4[i]])
    body5.set_data([x5[i]],[y5[i]])
    body6.set_data([x6[i]],[y6[i]])
    body7.set_data([x7[i]],[y7[i]])
    body8.set_data([x8[i]],[y8[i]])
    traj.set_data([x8[:i]],[y8[:i]])
    
        
    return body1,body2,body3,body4,body5,body6,body7,body8,body9,traj

ani=FuncAnimation(fig,animate,frames=len(t),init_func=init,blit=True,interval=60)



plt.show()
