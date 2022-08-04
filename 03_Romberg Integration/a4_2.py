import numpy as np
from scipy.special import *
from matplotlib.pyplot import *

def func(u):
	if u < 1:
		return 2*(jv(3,2.7*u)**2)*u
	else:
		return 2*(abs(jv(3,2.7)/kv(3,1.2))**2)*u*kv(3,1.2*u)**2
		
u = np.logspace(-6,6,1000)

for i in u:
	semilogy(i,func(i))

show()
