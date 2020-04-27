import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
plt.rcParams['legend.fontsize'] = 10

class Config:
    R=10
    H=1
    len_spring=50
    n_points=1000
    POINTS_CHOSEN = [0,784]

def simulate_spring(R, H, len_spring, n_points):
    # Parametric representation of points on spring is (R*cos(t),R*sin(t),H*t)
    t = np.linspace(0, len_spring, n_points+1)
    x = R * np.cos(t)
    y = R * np.sin(t)
    z = H*t
    return t, np.stack([x,y,z])

def plot_spring(data,config=None):
    x,y,z = data
    fig = plt.figure(figsize=(10,10))
    ax = fig.gca(projection='3d')
    ax.scatter3D(x, y, z, label='spring',c='b',s=5)
    ax.plot3D(x[:x.shape[0]//2], y[:x.shape[0]//2], z[:x.shape[0]//2], 'gray')

    ax.legend()
    if config:
        x_p,y_p,z_p = x[config.POINTS_CHOSEN], y[config.POINTS_CHOSEN], z[config.POINTS_CHOSEN]
        for (x_,y_,z_) in zip(x_p,y_p,z_p):
            ax.scatter3D([x_], [y_], [z_], c='r', s=200, marker='x')
    fig.savefig("spring_scatter.png")


def getData():
    config = Config()
    t, data = simulate_spring(config.R, config.H, config.len_spring, config.n_points)
    plot_spring(data,config)
    return data

def main():
    pts = getData()
    print(pts[0][0])
    print(pts[1][0])
    print(pts[2][0])

    print(pts[0][784])
    print(pts[1][784])
    print(pts[2][784])
main()