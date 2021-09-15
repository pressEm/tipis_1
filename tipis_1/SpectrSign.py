import pylab
from numpy.fft import rfft
from numpy import linspace, sin, pi

def spectr(y, place):
    x = linspace(0, 3 * pi, 100)
    f = rfft(y)
    freq = pylab.np.fft.rfftfreq(len(y), d=x[1] - x[0])
    pylab.subplot(4, 2, place)
    pylab.plot(freq, abs(f) ** 2)

def graph(num):
    period = 2**num
    x = linspace(0, 3*pi, 100)
    print(x)
    y = sin(period * x)

    pylab.subplot(4, 2, num*2+1)
    pylab.plot(x, y)

    spectr(y, (num+1)*2)

for i in range(0,4):
    graph(i)
pylab.show()
