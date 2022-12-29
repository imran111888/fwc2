import numpy as np
import math

# Initialize the number of items to choose from
n = 2
# Initialize the number of possibilities to choose
x = range(n + 1)
p=0.167   #probability of getting six on dises
q=0.833   #probability of getting nons six on disces

#print(x)

mu = 0
for i in x:
    print(x[i])
    nCx = math.comb(n,x[i])
    Pxi = nCx*p**x[i]*q**(n-x[i])
    Xi_Pxi= x[i]*Pxi
    print(Pxi)
    mu = mu + Xi_Pxi
    if i==3:
        break    
    i+=1
print("mean expectation of getting six on disc", mu)    
 



