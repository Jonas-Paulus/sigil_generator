import numpy as np
import matplotlib.pyplot as plt

def print_circle(ax, r):
    phi = np.linspace(0,2*np.pi, 10000)
    x = np.sin(phi)*r
    y = np.cos(phi)*r
    ax.plot(x,y)


print("hello world")
fig, ax = plt.subplots()
print_circle(ax, 1)
plt.show()

