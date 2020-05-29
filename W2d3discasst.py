#clear variables
import gc
gc.collect()

#close all plots
import matplotlib.pyplot as plt
plt.close("all")

#clear output screen
print("\033c")

from numpy import*

x=arange(0,10.5,0.5)
N=len(x)

# print ('N=' +str(N))

# print('x=' +str(x))
for i in range(N):
	y=x[i]
	print('y= ' +str(y))
	z=y**2
	print('z= ' +str(z))
