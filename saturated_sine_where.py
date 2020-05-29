from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2*sin(2*pi*t)

import copy
y_sat = copy.copy(y)

figure(1)
clf()
plot(t,y,'r--')

# find indices where y is above 1.5
inds1 = where(y>1.5)[0]

#set the value of y for those indices to 1.5
y_sat[inds1] = 1.5

#repeat for the negative case
inds2 = where(y < -1.5)[0]
y_sat[inds2]=-1.5

#plot my results

figure(1)
clf()
plot(t, y,'r--')
plot(t, y_sat, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()


