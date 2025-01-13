import numpy as np
import math
class LogisticRegression:
    def fit(self,x,y):
        x=np.array(x)
        y=np.array(y)

        mx=int(x.mean())#mean of x(total bill)

        my=int(y.mean())#mean of y(Tip amount)

        bd=x-mx   #bill deviations
       
        td=y-my   #Tip deviations
     
        dp=bd*td  #bill & tip deviations product
        
        sum_dp=dp.sum()#Sum of bill & tip deviations product

        bd_sqr=bd**2   #bill deviations sqr

        sum_bd_sqr=bd_sqr.sum()#Sum of bill deviations sqr

        self.S=sum_dp/sum_bd_sqr #SLOPE (b1)/BEST FIT LINE
        self.I=my-(self.S*mx) #INTERCEPT (b0)/BEST FIT LINE
        
    def predict(self,yp):
         pre=math.exp(self.I+self.S*yp)/(1+math.exp(self.I+self.S*yp)) #your Regression line(Prediction Value)
         return pre

     
