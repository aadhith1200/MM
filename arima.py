# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 18:24:19 2022

@author: bhava
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from sklearn.linear_model import LinearRegression
from statsmodels.graphics.tsaplots import plot_predict

    

file = pd.read_csv(r'C:\Users\bhava\OneDrive\Desktop\sem-9\Lab\Mathematical Modelling\WS-7\Trent_dataset.csv')
Close=np.array(file['Close Price'])
#Close=np.array([22,23,21,31,23,42,45,34,57,58,62,55])
y=np.array(Close)


sm.graphics.tsa.plot_acf(y,lags=2)
sm.graphics.tsa.plot_pacf(y,lags=2)

p=1
q=1
d=1

model=ARIMA(y,order=(p,q,d))   
model_fit=model.fit()
plot_predict(model_fit, dynamic = False)
plt.show()

residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()
# density plot of residuals
residuals.plot(kind='kde')
plt.show()
# summary stats of residuals
print(residuals.describe())

output=model_fit.forecast()
y_p=output[0]

print(y_p)
