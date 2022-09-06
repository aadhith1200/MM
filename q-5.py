print("Worksheet 3 problem 4")
import numpy as np
import matplotlib.pyplot as plt

x = np.array([57.9,108.2,149.6,227.9,778.1,1428.2,2837.9,4488.9])
y = np.array([88,225,365,687,4329,10753,30660,60150])

x=np.log2(x)
y=np.log2(y)

mymodel = np.poly1d(np.polyfit(x, y, 1))

plt.plot(x, y, 'bo',label='yi')
plt.plot(x,mymodel(x),  label="precictedY", color='green')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper right', ncol=2)
plt.title('Linear Regression')
plt.show()

predictedY=mymodel(x)
ans=np.exp2(mymodel.coefficients)
print(mymodel.coefficients)
print("a is ",ans[0]," \nb is ",ans[1])
