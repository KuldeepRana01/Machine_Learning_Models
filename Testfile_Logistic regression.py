import numpy as np
import pandas as pd
from Logisticregression_Model import LogisticRegression
import math
df = pd.read_csv("d:/data/CS.csv")
x=df['CreditScore']
y=df['Approved']
# print(x)
# print(y)
r=LogisticRegression()
r.fit(x,y)
print('Intercept:',r.I)
print('Slope:',r.S)
res=r.predict(850)
print('Prediction Value:',res)