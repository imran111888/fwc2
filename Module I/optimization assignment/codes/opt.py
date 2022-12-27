#Python libraries for math and graphics
import numpy as np
from sympy import Symbol,solve,diff
import matplotlib.pyplot as plt
from numpy import linalg as LA
from math import *
import sys               #for path to external scripts
#import cvxpy  as cp

#whils using termux
import subprocess
import shlex
sys.path.insert(0,'/home/shreyash/Desktop/matrix/gvv/cbse-papers/CoordGeo')         #path to my scripts

#local imports
#from line.funcs import *
#from triangle.funcs import *
#from conics.funcs import conic_quad
#Gradient ascent

#Defining f(x)
def f(x):
	return x**25*(1-x)**75
label_str = "$x**25*(1-x)**75)$"

#For maxima using gradient ascent
cur_x = 0.25
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 25*x**24*(1-x)**74*(1-4*x)           

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

max_val = f(cur_x)
print("Maximum value of f(x) is ", max_val, "at","x =",cur_x)


###########plot###
#Plotting f(x)
x=np.linspace(-1,5,100)
y=f(x)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()

#if using termux
plt.savefig('/sdcard/download/opt/fig.pdf')
subprocess.run(shlex.split("termux-open (/sdcard/download/opt/fig.pdf"))
#else
plt.show()

