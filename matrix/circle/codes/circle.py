

#Code by GVV Sharma
#November 12, 2019
#released under GNU GPL
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import linalg as LA
import shlex
#from coeffs import *

def dir_vec(A,B):
  return B-A
omat=np.array([[0,1],[-1,0]])
def norm_vec(A,B):
  return np.matmul(omat, dir_vec(A,B)) 
#if using termux
import subprocess
import shlex
#end if


def line_dir_pt(m,A,k1,k2):
  len = 10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ
#circle points
C=np.array([1,2])
r=np.sqrt([2])
x_circ=circ_gen(C,r)

#Line points
n = np.array([2,-3]) 
c = -4
A = np.array([0,4/3]) 
P = np.array([2,3]) 
m = (omat@n)
k1 = -1.5
k2=1
R = ((np.outer(m,m)-np.outer(n,n))@P+2*c*n)/(np.linalg.norm(n)**2)
x_L = line_dir_pt(m,A,k1,k2)
#line2 points
n1=np.array([1,-2])
c1=-3
A1=np.array([0,1/2])
p1=np.array([2,3])
m1=omat@n
k1 = -1.5
k2=1
A=np.array([2,3])
B=np.array([1,2])
#R1=((np.outer(m1,m1)-np.outer(n1,n1))@p1+2*c1*n1)/(np.linalg.norm(n1)**2)
plt.axline(B,A,color='yellow',linestyle='-',label='$LINE2$')
plt.axline(B,slope=1/2, color='green', linestyle='--',label='$LINE2$')
x_M = line_dir_pt(n1,p1,k1,k2)
#Hero's formulA

R1=(p1+(2*((c1-(n1@p1))/((LA.norm(n1)**2))))*n1)

print(R)
print(R1)
plt.plot(x_L[0,:],x_L[1,:],label='$L$')

plt.plot(x_M[0,:],x_M[1,:],label='$M$')
plt.plot(R1[0],R1[1],'o',label='R')
plt.plot(2.15,2.75,'.',label='p`')
plt.plot(2.2,2.6,'.',label='r`')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.1), R[1] * (1 - 0.1) , 'R')


#plt.plot(p1[0], p1[1], 'o')
#plt.text(p1[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'p1')
#plt.plot(R1[0], R1[1], 'o')
#plt.text(R1[0] * (1 + 0.1), R1[1] * (1 - 0.1) , 'R1')
# use set_position 
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')

#Plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],'r',label='$Circle1$')
o=np.array([2,3])
#Labeling the coordinates
tri_coords = np.vstack((o, C)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['o(2,3)','C(1,2)']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')
#if using termux
plt.savefig('/sdcard/download/Circle/fig1.pdf')
#plt.savefig('/sdcard/download/Circle/figure1.pdf')
subprocess.run(shlex.split("termux-open /sdcard/download/Circle/figure1.pdf"))
#else
#plt.show()

