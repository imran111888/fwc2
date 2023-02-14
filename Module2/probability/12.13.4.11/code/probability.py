import numpy as np
import random

k = [0,1,2]                   # random variable
P_k = [25/36,10/36,1/36] # PDF             
n = 1000 #trials

mean_calculated = k[0]*P_k[0]+k[1]*P_k[1]+k[2]*P_k[2]
print("Mean number of heads in three tosses of a coin is", mean_calculated)


#Simulating samples 
S = np.random.choice(k, p=P_k, size=n)          
Samples = list(S)

#Generating PDF through simulated samples
P_0 = Samples.count(0)/n
P_1 = Samples.count(1)/n
P_2 = Samples.count(2)/n


mean_simulated = k[0]*P_0+k[1]*P_1+k[2]*P_2
print("Mean through simulation is", mean_simulated)
  
