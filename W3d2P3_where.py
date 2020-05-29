from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

import copy
y_pass = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')

# find indices where y is below 0.5
inds1 = where(y<0.5)[0]

#set the value of y for those indices to 0
y_pass[inds1] = 0

#plot results

figure(1)
clf()
plot(t, y,'r--')
plot(t, y_pass, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()


