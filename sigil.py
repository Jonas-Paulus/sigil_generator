import numpy as np
import matplotlib.pyplot as plt
golden = (1 + 5 ** 0.5) / 2
def print_circle(ax, r):
    phi = np.linspace(0,2*np.pi, 10000)
    x = np.sin(phi)*r
    y = np.cos(phi)*r
    ax.plot(x,y)

def print_polygon(ax, n,r, s = 0, phi0 = -np.pi/2):
    if (n+1)%(s+1) == 0:
        phi = np.linspace(0,2*np.pi,n+1)*(s+1) + phi0
        x = np.cos(phi)*r
        y = np.sin(phi)*r
        ax.plot(x,y)
    else:
        m = n//(s+1)
        for i in range(m):
            print(i)
            print_polygon(ax, m,r = r,phi0 = -np.pi/2+i*2*np.pi/n)

    
print("hello world")
fig, ax = plt.subplots()
print_circle(ax, 1)
print_polygon(ax, 9, 1, 2)
#print_polygon(ax, 9, 1, 1)
#print_circle(ax, 1/golden)
#print_circle(ax, 1/golden**2)
#print_circle(ax, 1/golden**3)
plt.gca().set_aspect('equal')
plt.show()

