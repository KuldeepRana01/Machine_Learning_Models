import numpy as np
import math
class LinearRegression:
    def fit(self,x,y):
        x=np.array(x)
        y=np.array(y)

        mx=int(x.mean())#mean of x(total bill)
        print(mx)

        my=int(y.mean())#mean of y(Tip amount)
        print(my)

        bd=x-mx   #bill deviations
        print(bd)

        td=y-my   #Tip deviations
        print(td)

        dp=bd*td  #bill & tip deviations product
        print(dp)

        sum_dp=dp.sum()#Sum of bill & tip deviations product
        print(sum_dp)

        bd_sqr=bd**2   #bill deviations sqr
        print(bd_sqr)

        sum_bd_sqr=bd_sqr.sum()#Sum of bill deviations sqr
        print(sum_bd_sqr)

        self.S=sum_dp/sum_bd_sqr #SLOPE (b1)/BEST FIT LINE
        self.I=my-(self.S*mx) #INTERCEPT (b0)/BEST FIT LINE
        
    def predict(self,yp):
         pre=self.I+(self.S*yp) #your Regression line(Prediction Value)
         return pre

     
