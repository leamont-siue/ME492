#saturate sine wave for loop using enumerate
from matplotlib.pyplot import*
from numpy import *

t=arange(0,1,0.01)
y = 2*sin(2*pi*t)

N = len(y)
y_pass=zeros(N)

for i, y_i in enumerate(y):
	if y_i < 0.5:
		y_pass[i] = 0
	else:
		y_pass[i] = y_i

#still not great; more loops = more computational time
#min loops is best

figure(1)
clf()
plot(t, y,'r--')
plot(t, y_pass, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()
