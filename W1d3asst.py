from matplotlib.pyplot import*
from numpy import*

t=arange(1,3,0.02)

T=6*np.log(t)-7*exp(0.2*t)

figure(1)
clf()

plot(t,T)
title('Montgomery-Plot')
xlabel('Time (min.)')
ylabel('Temperature (Celsius)')
show()
print('Hello World! I just wrote my first Python program. Yayyyyyyyy')
print('Leanne')
