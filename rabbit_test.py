import numpy as np
import matplotlib.pyplot as plt
def function(growth_rate,x):
    x = growth_rate*x*(1-x)
    return x

def roundoff(x):
    return int(x*10**4)/10**4

growth_rate_constants = np.linspace(0,2.22,100)

equilibrium_constants = []

count = 0

for j in growth_rate_constants:
    
    b = 0.9
    temp  = 0.1
    count += 1
    while  b != temp:

        temp = b

        b = roundoff(function(j,b))
    

    equilibrium_constants.append(b)
    print(count)
    
        
plt.plot(growth_rate_constants,equilibrium_constants)
plt.show()