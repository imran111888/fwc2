#code by mohammad imran using python
#python libararies for math and graphics
import numpy as np
import math
from math import pow
import matplotlib.pyplot as plt
from numpy import linalg as LA 
#generating points on circle

#Generating points on a circle
def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
#Input parameters
c=np.array([-8,-6])
r=np.sqrt(5)
x_circ1=circ_gen(c,r)
# use set_position 
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

#finding point on circle
q=np.array([1,7])
u=-7
m=np.array([1,2])

p=q+u*m

#generating tangent of circle
def line_gen(A,B):
    len =10
    dim = A.shape[0]
    x_AB = np.zeros((dim,len))
    lam_1 = np.linspace(0,1,len)
    for i in range(len):
      temp1 = A + lam_1[i]*(B-A)
      x_AB[:,i]= temp1.T
    return x_AB

#ploting tangent

x_pq = line_gen(p,q)
#generating parabola
def parab_gen(y,a):
    y = x**2+6
    return y

#  plotting parabola
simlen=100
a=6
x= np.linspace(-5,5,simlen)
y=x**2+a
plt.plot(x, y, label='Parabola')
#ploting common tangent to the circle and parabola
plt.plot(x_pq[0,:],x_pq[1,:],color='red',label='$common tangent$')

#Plotting the circle
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$Circle1$')
#o=np.array(([-6,-7]))
#Labeling the coordinates
tri_coords = np.vstack((c,p,q)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['c','p(-6,-7)','q(1,7)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,-20), # distance from text to points (x,y)
                 ha='left') # horizontal alignment can be left, right or center




plt.xlabel('$ X $')
plt.ylabel('$ Y $')
plt.legend()
plt.grid(True) # minor
plt.axis('equal')
plt.title('conics')
plt.savefig('/sdcard/download/conic/fig.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/download/conic/fig.pdf"))
plt.show()












































































































































