import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
import math


k = [10, 5, 15]
d = [2, 4, 4]
h = [0.3, 0.1, 0.2]
#y = [11.55, 20.00, 24.49]
y = []
a = [1, 2, 3]

def f(x):  
    val = (k[0]*d[0]/x[0] + h[0]*x[0]/2) + (k[1]*d[1]/x[1] + h[1]*x[1]/2) + (k[2]*d[2]/x[2] + h[2]*x[2]/2)
    print(f"F(x) = {val}")
    return val

def constraint(x):
    # sum should be less than 50
    # print(x)

    return 50 - np.sum(a*x)

def y_star(k, d, h):
  val = ((2 * k * d) / (h)) ** 0.5
  return val

#initial values

for i in range(len(k)):
  y.append(y_star(k[i], d[i], h[i]))

y

result = optimize.minimize(f, [1,1,1], constraints={"fun": constraint, "type": "ineq"}, method='SLSQP', bounds=((0, 10000), (0, 10000), (0, 10000)))
print(f"y values: {list(result['x'])}")
print()

y = result['x']
y

new_y = []

for i in range(len(y)):
  new_y.append(math.floor(y[i]))

new_y
