import numpy as np
import matplotlib.pyplot as plt

def print_circle(ax, r):
    phi = np.linspace(0,2*np.pi, 10000)
    x = np.sin(phi)*r
    y = np.cos(phi)*r
    ax.plot(x,y)

def print_polygon(ax, n,r, phi0 = -np.pi/2):
    phi = np.linspace(0,2*np.pi,n+1) + phi0
    x = np.cos(phi)*r
    y = np.sin(phi)*r
    ax.plot(x,y)


print("hello world")
fig, ax = plt.subplots()
print_circle(ax, 1)
print_polygon(ax, 5, 1)
plt.show()

