#saturate sine wave for loop using enumerate
from matplotlib.pyplot import*
from numpy import *

t=arange(0,1,0.01)
y = 2*sin(2*pi*t)

N = len(y)
y_sat=zeros(N)

for i, y_i in enumerate(y):
	if y_i > 1.5:
		y_sat[i] = 1.5
	elif y_i < -1.5:
		y_sat[i] = -1.5
	else:
		y_sat[i] = y_i



figure(1)
clf()
plot(t, y,'r--')
plot(t, y_sat, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()
