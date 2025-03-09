import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
#https://stackoverflow.com/questions/19353576/curved-text-rendering-in-matplotlib
golden = (1 + 5 ** 0.5) / 2


def print_circle(ax, r):
    phi = np.linspace(0,2*np.pi, 10000)
    x = np.sin(phi)*r
    y = np.cos(phi)*r
    ax.plot(x,y)

def print_polygon(ax, n,r, s = 0, phi0 = -np.pi/2):
    if (n)%(s+1)!= 0 or s==0:
        phi = np.linspace(0,2*np.pi,n+1)*(s+1) + phi0
        x = np.cos(phi)*r
        y = np.sin(phi)*r
        ax.plot(x,y)
        return [x,y]
    else:
        m = n//(s+1)
        x = np.empty(0,float)
        y = np.empty(0,float)
        for i in range(m):
            #print(i)
            points = print_polygon(ax, m,r = r,phi0 = -np.pi/2+i*2*np.pi/n)
            x = np.concatenate(x,points[0])
            y = np.concatenate(y,points[1])
        return [x,y]

fontfile = "/home/jonas/Desktop/Programmieren/fonts/daedra/Daedra.otf"
font = fm.FontProperties(fname=fontfile)

    
#print("hello world")
fig, ax = plt.subplots()
print_circle(ax, 1)
#print_polygon(ax, 9, 1, 3)
#print_polygon(ax, 9, 1, 2)
points = print_polygon(ax, 7, 1, 1)
#print_circle(ax, 1/golden)
#print_circle(ax, 1/golden**2)
#print_circle(ax, 1/golden**3)
#ax.plot(points[0], points[1])
circle = plt.Circle([0,-1],0.2,fc = "w", ec = "k", zorder = 5)
ax.add_patch(circle)

ax.set_xlabel("secret message", fontproperties = font, fontsize = 30)
plt.text(-0.13,
         -1.16,
         "walle\nwalle\nmanche\nstrecke", 
         fontproperties = font, 
         fontsize = 10,
         zorder = 10)
plt.gca().set_aspect('equal')
plt.show()

