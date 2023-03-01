import numpy as np
import matplotlib.pyplot as plt


n = 1000000     # Number of samples

U = np.random.uniform(0, 1, n)  # Generating samples of U
#print(U)

V = -2 * np.log(1 - U)          # Transforming U to V 
V_ascend = np.sort(V)           # Sorting V in ascending order
#print(V_ascend)

# Calculating the CDF of V through simulation
Pdf_simulated = np.ones(n)/n
Cdf_simulated = np.cumsum(Pdf_simulated)

# Calculating the theoretical CDF of V 
V_stepped = V_ascend[::int(n/50)]
Cdf_theory = 1 - np.exp(-V_stepped/2)  # Theoretical expression for cdf of V

# Plotting the CDF of V
plt.plot(V_ascend,Cdf_simulated,label='Simulated CDF')
plt.scatter(V_stepped, Cdf_theory, s=20, color='green', label='Theoretical CDF')
plt.grid() 
plt.xlabel('$V$')
plt.ylabel('$F_V(V)$')
plt.legend()
plt.savefig('/home/imran/module 1/probability/digital_comm/fig.pdf')
plt.show()
