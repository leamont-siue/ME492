from matplotlib.pyplot import*
from numpy import*

t = arange(0,1,0.01)
y1 = sin(2*pi*t)

figure(1)
clf
plot(t,y1)
xlabel('Time (sec.)')
savefig('fig1.png',dpi=200)

y2=1.5*cos(3*pi*t)

figure(2)
clf()
plot(t,y2)
xlabel('Time (sec.)')
ylabel('$y_2(t)$')
savefig('fig2.png',dpi=200)

show()
