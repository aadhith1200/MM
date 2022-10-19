import math

def y_star(k, d, h):
  val = ((2 * k * d) / (h)) ** 0.5
  return val

def reorder_point(y, d, l):
  t0 = y / d
  le = l

  if l > t0:
    n = math.floor(l / t0)
    le = l - n*t0
    
  pt = le * d
  return pt

def inventory_policy(y, d):
  print("\nOrder the quantity ", y, " whenever the inventory level drops to ", d, " units.")

def total_cost(d, k, h):
  val = (2 * d * k * h) ** 0.5
  return val



l = 35
d = 25
k = 120
h = 0.04

#y* 
y = math.floor(y_star(k, d, h))

#reorder point
rp = math.floor(reorder_point(y, d, l))

#total cost
tc = total_cost(d, k, h)

#finl ordering statement
inventory_policy(y, rp)

print("\nTotal cost is : ", tc)

