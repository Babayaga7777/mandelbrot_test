import numpy as np
import matplotlib.pyplot as plt


a = np.linspace(0,1,100)
temp = []

def function(growth_rate,x):
    x = 2.7*x*(1-x)
    return x
b = 0.99
for i in range(100):
    temp.append(b)
    b = function(b)

    
plt.scatter(a, temp, color = 'red')
# plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()