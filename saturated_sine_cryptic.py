from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.001)
y=2*sin(2*pi*t)

#create a copy of y for the original signal
#changes to copy won't affect the values in the original
import copy
y_sat = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')

#for any index where this condition is true, substitute this value
y_sat[y_sat > 1.5] = 1.5
y_sat[y_sat < -1.5] = -1.5

#plot results & show
plot(t,y_sat,linewidth=2.0, label= '$y(t)$')
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)
show()
