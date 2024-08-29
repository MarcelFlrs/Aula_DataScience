# .*. coding: cp1252 .*.
# Exemplo de interpolacao
'''

Documentação explicando o codigo

'''

from matplotlib import *
from pylab import *
from numpy import *
from scipy import *

from scipy import stats

#create a (discreet) random variable with poissionian distribution
X = stats.poisson(3.5)

n = arange(0,15)
fig, axes = subplots(3,1, sharex=True)

axes[0].step(n,X.pmf(n))
axes[1].step(n, X.cdf(n))
axes[2].hist(X.rvs(size=1000))

show()



y = stats.norm()

x = linspace(-5,5,100)
fig, axes = subplots(3,1, sharex=True)

axes[0].step(n,x.pmf(n))
axes[1].step(n, x.cdf(n))
axes[2].hist(y.rvs(size=1000), bins=50)

show()


x.mean(), x.std(), x.var()

y.mean(), y.std(), y.var()

t_statistc, p_value = stats.ttest_ind(x.rvs(size=1000), y.rvs(size=1000))
print("t_statistc = "), t_statistc
print("p_value"), p_value