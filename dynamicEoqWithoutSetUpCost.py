# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:41:23 2022

@author: bhava
"""

r=[90,100,120,110]
o=[50,60,80,70]
d=[100,190,210,160]

cr=6
co=9
hc=10

pos=0
tc=0

for i in range(len(r)):
    print("\nIteration - ", i+1)
    temp=d[i]
    print(temp)
    temp-=r[i]
    tc+=r[i]*cr
    r[i]=0
    if(temp!=0):
        if(temp>o[i]):
            temp-=o[i]
            tc+=o[i]*co
            o[i]=0
        else:
            tc+=temp*co
            o[i]-=temp
            temp=0
    if(temp!=0):
        if(temp>o[pos]):
            temp-=o[pos]
            tc+=((i-pos)*hc+co)*o[pos]
            o[pos]=0
            temp=0
        else:
            o[pos]-=temp
            tc+=((i-pos)*hc+co)*temp
            temp=0
    if(o[pos]==0 and o[i]!=0):
        pos=i
    else:
        for j in range(pos,i):
            if(o[j]!=0):
                pos=j
                
    print(tc, pos)
    print("----------")
print(tc)
