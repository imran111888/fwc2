#code by mohammad imran using python

#To find the equation of a line which passes through point(3,-2) and intercts on x axes and inclined to a line at 60 degres.


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA
import math
import subprocess
import shlex

#we know equation of straight line is ntranspose(X)=C
#given equation of straight is m=sqrt(3)x+y=1
#from above equatin  we know that mtranspose(sqrt(3),1)=1
#given unknow will passes through point (3,-2) and intersects x axis (x,0)
#from above two conditions we get
#n=np.transpose([(1/x),(3-x/2*x)])
#given angle between two vectors is 60 degres
#by angle relation we find the x value x=2/sqrt(3)+3


#Input vectors
x=np.array([(2/(np.sqrt(3)))+3])
n=np.array([(1/x),(3-x)/(2*x)])
c=np.array([2+(3*np.sqrt(3))])
print("equation of line is ")
print(n,'x=',c)

#to find point of intersection between two lines
A=np.array([[np.sqrt(3),1],[np.sqrt(3),-1]])
B=np.array([1,2+(3*np.sqrt(3))])
D=np. linalg. inv(A) #d=inverse matrix of A
P=D@B

#########################################################################
####plotting part####

def line_gen(A,B):
   len =10
   dim = A.shape[0]
   x_AB = np.zeros((dim,len))
   lam_1 = np.linspace(0,1,len)
   for i in range(len):
     temp1 = A + lam_1[i]*(B-A)
     x_AB[:,i]= temp1.T
   return x_AB



#Given points
P = np.array(([0,1]))
Q = np.array(([2.36602540378,3.09807621135]))
R = np.array(([3,-2]))


x_PQ = line_gen(P,Q)
#x_PR = line_gen(P,R)
x_QR = line_gen(Q,R)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
#plt.plot(x_PR[0,:],x_PR[1,:],label='$PR$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')

#Labeling the coordinates
tri_coords = np.vstack((P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xlabel('$x_axis$')
plt.ylabel('$y_axis$')
plt.legend(loc='best')
plt.grid() 
plt.axis('equal')
plt.title('equation of straight line')
plt.savefig('/home/imran/matrix/figure.pdf')  
#subprocess.run(shlex.split("termux-open /home/imran/matrix/figure.pdf"))
plt.show()





























































































