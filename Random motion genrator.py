import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.interpolate import make_interp_spline

# 1. Setup timing and waypoints
num_waypoints = 10     # Number of random points to visit
total_frames = 300     # Higher frame count for a smoother framerate

# Create time arrays for the waypoints and the smooth frames
t_waypoints = np.linspace(0, 1, num_waypoints)
t_smooth = np.linspace(0, 1, total_frames)

# 2. Generate random waypoints (keeping them slightly inside the -2 to 2 bounds)
x1_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
y1_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
x2_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
y2_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
x3_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
y3_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
x4_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
y4_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
x5_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8
y5_rand = (2 * np.random.rand(num_waypoints) - 1) * 1.8

# 3. Create smooth paths using Cubic Spline Interpolation
x1 = make_interp_spline(t_waypoints, x1_rand, k=3)(t_smooth)
y1 = make_interp_spline(t_waypoints, y1_rand, k=3)(t_smooth)
x2 = make_interp_spline(t_waypoints, x2_rand, k=3)(t_smooth)
y2 = make_interp_spline(t_waypoints, y2_rand, k=3)(t_smooth)
x3 = make_interp_spline(t_waypoints, x3_rand, k=3)(t_smooth)
y3 = make_interp_spline(t_waypoints, y3_rand, k=3)(t_smooth)
x4 = make_interp_spline(t_waypoints, x4_rand, k=3)(t_smooth)
y4 = make_interp_spline(t_waypoints, y4_rand, k=3)(t_smooth)
x5 = make_interp_spline(t_waypoints, x5_rand, k=3)(t_smooth)
y5 = make_interp_spline(t_waypoints, y5_rand, k=3)(t_smooth)




# 4. Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

body1, = ax.plot([], [], 'ro', markersize=10)
body2, = ax.plot([], [], 'go', markersize=10)
body3, = ax.plot([], [], 'bo', markersize=10)
body4, = ax.plot([], [], 'ko', markersize=10)
body5, = ax.plot([], [], 'co', markersize=10)


def init():
    body1.set_data([], [])
    body2.set_data([], [])
    body3.set_data([], [])
    body4.set_data([], [])
    body5.set_data([], [])
    
    return body1,body2,body3,body4,body5

def animate(i):
    body1.set_data([x1[i]], [y1[i]])
    body2.set_data([x2[i]], [y2[i]])
    body3.set_data([x3[i]], [y3[i]])
    body4.set_data([x4[i]], [y4[i]])
    body5.set_data([x5[i]], [y5[i]])
    
    return body1, body2,body3,body4,body5

# interval=20 means 50 frames per second (1000ms / 20 = 50 fps)
ani = FuncAnimation(fig, animate, frames=total_frames, init_func=init, blit=True, interval=20)

plt.show()