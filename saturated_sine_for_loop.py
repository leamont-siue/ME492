#saturated_sine_for_loop
from matplotlib.pyplot import *
from numpy import *

t = arange(0,1,0.01)
y = 2.0*sin(2*pi*t)


N=len(y)
#create an array the same dimensions
#but with all zeros we'll change along the way

y_sat = zeros(N)

for i in range(N):
	y_i = y[i]
	if y_i > 1.5:
		y_sat[i] = 1.5
	elif y_i < -1.5:
		y_sat[i] = -1.5
	else:
		y_sat[i]=y_i

figure(1)
clf()
plot(t, y,'r--')
plot(t, y_sat, label='$y(t)$', linewidth=2.0)
ylabel('$y(t)$')
xlabel('Time(sec.)')
legend(loc=1)

show()
