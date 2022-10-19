

import math
import matplotlib.pyplot as plt


inf = 10000000

def y_star(k, d, h):
  val = ((2 * k * d) / (h)) ** 0.5
  return val

def tc(d, c, k, h, y):
  val = (d * c) + (k * d / y) + (h * y / 2) 
  return val

def compute_Q(d, k, h, c1, c2, y):
  a = 1
  b = (2 / h) * ((d * c2) - tc(d, c1, k, h, y))
  c = ((2 * k * d) / h)

  roots = [((-b + (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a)), ((-b - (b ** 2 - (4 * a * c)) ** 0.5) / (2 * a))]
  Q = 0

  for i in roots:
    if i > y:
      Q = i

  return Q

def reorder_pt(l, d, y):
  t0 = y / d
  le = l

  if l > t0:
    n = math.floor(l / t0)
    le = l - n * t0
    return le * d

  else:
    return le * d

def compute_optimum(q, Q, ym):
  if (0 < q < ym) or (Q < q < inf):
    y = ym
  else:
    y = q

  return y

d = 30
h = 0.05
k = 100
c1 = 10
c2 = 8
q = 500
l = 21

ym = y_star(k, d, h)
print(ym)

Q = compute_Q(d, k, h, c1, c2, ym)

y_final = compute_optimum(q, Q, ym)

r_pt = math.floor(reorder_pt(l, d, y_final))

print("Order ", y_final, " units of item if the inventory level falls below ", r_pt, " units.")

y1 = [i for i in range(1, q)]
y2 = [i for i in range(q, 1000)]
x_vals = [i for i in range(y_final-490, y_final+1000)]

vals_1 = [tc(d, c1, k, h, i) for i in x_vals]
vals_2 = [tc(d, c2, k, h, i) for i in x_vals]

plt.plot(x_vals, vals_1 , label="C1")
plt.plot(x_vals, vals_2 , label='C2')
leg=plt.legend()
