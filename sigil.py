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

class polygramm():

    def __init__(self, r, p, q=1, phi0= -np.pi/2):
        self.p = p
        self.r = r
        self.s = q
        self.phi0 = 0
        
        phi = np.linspace(0,2*np.pi,p+1) + phi0
        self.outer_points = np.zeros([p,2], float)
        self.outer_points[:,0] = np.cos(phi[:-1])*r
        self.outer_points[:,1] = np.sin(phi[:-1])*r
        self.lines = [[i, (i+q)%p] for i in range(p)]
        self.calc_intersecs(self.outer_points, self.lines)

    
    def calc_intersecs(self, points, lines):
        inner_points = np.zeros([self.p,2])
        for i in range(len(lines)):
            #print(i)
            A1 = points[lines[i][0],:]
            A2 = points[lines[i][1],:]
            B1 = points[lines[(i+1)%self.p][0],:]
            B2 = points[lines[(i+1)%self.p][1],:]
            #print(A1)
            Y = A1-B1
            M = np.array([B2-B1, A2-A1])
            #print(M)
            x = np.linalg.solve(M.T,Y)
            inner_points[i] = A1 + x[0]*(A2-A1)
        self.inner_points = inner_points
        rad = np.average(np.linalg.norm(self.inner_points, axis = 1))
        self.intersec_radius = rad

    def plot(self,ax):
        for line in self.lines:
            ax.plot(self.outer_points[line,0], 
                    self.outer_points[line,1],
                    "k")
    def mark_inner_points(self, ax):
        ax.plot(self.inner_points[:,0],
                self.inner_points[:,1], "g.")
    
def text_along_circle(ax, text, r, **kwargs):
    fig, imax = plt.subplots()
    rend = fig.canvas.get_renderer()
    t = imax.text(0.5, 0.5, 'test')

    bb = t.get_window_extent(renderer=rend)
    width = bb.width/5
    height = bb.height

    dphi = 2*np.pi*0.022
    phi = -np.arange(len(text)) *dphi + np.pi/2 + dphi*len(text)/2
    for i in range(len(text)):
        ax.text((r+0/2)*np.cos(phi[i]), 
                (r+0/2)*np.sin(phi[i]),
                text[i], 
                rotation = (phi[i]-np.pi/2)*180/np.pi,
                verticalalignment='center', 
                horizontalalignment='center',
                **kwargs)





fontfile = "/home/jonas/Desktop/Programmieren/fonts/daedra/Daedra.otf"
font = fm.FontProperties(fname=fontfile)

    
#print("hello world")
fig, ax = plt.subplots()
print_circle(ax, 1)
#print_polygon(ax, 9, 1, 3)
#print_polygon(ax, 9, 1, 2)
gramma = polygramm(1, 10, 3)
gramma.plot(ax)
gramma.mark_inner_points(ax)
gramma2 = polygramm(gramma.intersec_radius, 5, 2, phi0 = np.pi/2)
gramma2.plot(ax)
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

text_along_circle(ax, 
                  "Who ever reads this is forced to amaze",
                  1.1,
                  #fontproperties = font, 
                  fontsize = 25)
plt.gca().set_aspect('equal')
plt.show()

