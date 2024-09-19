import matplotlib.pyplot as plt
from pylab import *

ent1 = arange(0., 7., .1)
sai1 = cos(ent1)
sai2 = sin(ent1)
dif = sai2 - sai1

subplot(211)

plot(ent1, sai1, 'bo:', ent1, sai2, 'g^-')

legend(['Cossenos', 'Senos'])

subplot(212)

bar(arange(len(dif))+ .5, dif, .5, color='#ccbbaa')

savefig('graf.png')

