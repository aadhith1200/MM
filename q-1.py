# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:57:43 2022

@author: bhava
"""
import math
import matplotlib.pyplot as pt
from scipy import stats

year=[1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995]
Expenditure	=[731,782,833,886,956,1049,1159,1267,1367,1436,1505]

def Forward_Interpolation(Expenditure):
    diff=[]
    diff.append(Expenditure)
    k=0
    while(k<=len(diff)):
        j=diff[k]
        dummy=[]
        if(len(j)>1):
            for i in range(0,len(j)-1):
                temp=j[i+1]-j[i]
                dummy.append(temp)
            k+=1
            diff.append(dummy)
           
        else:
            return diff

def Predict(x,diff):
    u=(x-year[0])/(year[1]-year[0])
    j=0
    u_val=u
    value=diff[0][0]
    for i in range(1,len(diff)):
        if(j==0):
            value+=(u/math.factorial(j+1))*diff[i][0]
        else:
            value+=(u_val*(u-j)/math.factorial(j+1))*diff[i][0]
            u_val*=(u-j)
        j+=1
    return value

#full year
diff=Forward_Interpolation(Expenditure)

Expenditure_P=[]
for i in (year):
    Expenditure_P.append(Predict(i,diff))


pt.title('Interpolation')
pt.plot(year,Expenditure)
pt.plot(year,Expenditure_P)
pt.show()
 
#t-test
t1,p1=stats.ttest_ind(Expenditure,Expenditure_P)
print("T-test value: ",p1) 
print("Its a perfect fit") 
       
#only till 1993
diff=[]
diff=Forward_Interpolation(Expenditure[:9])

Expenditure_P=[]
for i in (year):
    Expenditure_P.append(Predict(i,diff))


pt.title('Interpolation-2')
pt.plot(year,Expenditure)
pt.plot(year,Expenditure_P)
pt.show()

#t-test
t1,p1=stats.ttest_ind(Expenditure,Expenditure_P)
print("T-test value: ",p1) 
   
        