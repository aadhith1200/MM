# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:58:48 2022

@author: bhava
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as pt
from scipy import stats
from sklearn.linear_model import LinearRegression

file = pd.read_csv(r'C:\Users\bhava\OneDrive\Desktop\sem-9\Lab\Mathematical Modelling\WS-4\Trent_dataset.csv')

Open=np.array(file['Open Price'])
Close=np.array(file['Close Price'])
High=np.array(file['High Price'])
Low=np.array(file['Low Price'])
def calculate_y(Temp):
    y0=[]
    for i in range(0,len(Temp)):
        dummy=0
        dummy=intercept+(slope*Temp[i])
        y0.append(dummy)
    return y0
    
        
#close vs open{linear Reg}

slope,intercept,r,p,std_err=stats.linregress(Open,Close)
Close_P=calculate_y(Open)

pt.title('close vs open')     
t1,p1=stats.ttest_ind(Close,Close_P)
print("T-test value(Linear Reg): ",p)   
pt.scatter(Open,Close)
pt.plot(Open,Close_P)
pt.show()
corr1=np.corrcoef(Open,Close,rowvar=False)

print("Coorelation (Open vs Close): ",corr1)
#High vs Low{linear Reg}


slope,intercept,r,p,std_err=stats.linregress(Low,High)
High_P=calculate_y(Low)

pt.title('High vs Low')       
pt.scatter(Low,High)
pt.plot(Low,High_P)
pt.show()
corr2=np.corrcoef(Low,High,rowvar=False)
print("Coorelation (Low vs High): ",corr2)
#(open,low,high) vs Close

def MultipleLinearReg():
    y0=[]
    for i in range(0,len(Open)):
        dummy=mlr.intercept_+(mlr.coef_[0]*Open[i])+(mlr.coef_[1]*High[i])+(mlr.coef_[2]*Low[i])
        y0.append(dummy)
    return y0

Data=pd.DataFrame([Open,High,Low])
#print(Data)
mlr = LinearRegression()
mlr.fit(Data.transpose(),Close)
print(mlr.intercept_)
print(mlr.coef_)

y0=MultipleLinearReg()

t,p=stats.ttest_ind(Close,y0)
print("T-test value: ",p)

pt.title('Multiple Linear Regression')      
pt.plot(np.array(file['Date']),y0)
pt.plot(np.array(file['Date']),Close)
pt.xlabel("Date")
pt.ylabel("Close Price")
pt.show()

#trend
if(p<p1):
    print("Linear Reg is better is better in prediction")
else:
    print("Multiple Linear Regression is better in prediction")