import numpy as np
x=np.array([34,108,64,88,99,51])
y=np.array([5,17,11,8,14,5])

mx=int(x.mean())#mean of x(total bill)

my=int(y.mean())#mean of y(Tip amount)

bd=x-mx   #bill deviations

td=y-my   #Tip deviations

dp=bd*td  #bill & tip deviations product

sum_dp=dp.sum()#Sum of bill & tip deviations product

bd_sqr=bd**2   #bill deviations sqr

sum_bd_sqr=bd_sqr.sum()#Sum of bill deviations sqr

S=sum_dp/sum_bd_sqr #SLOPE (b1)/BEST FIT LINE
print('Slope:',S)

I=my-(S*mx) #INTERCEPT (b0)/BEST FIT LINE
print('Intercept:',I)

pre=I+(S*34) #your Regression line(Prediction Value)
print('Prediction Result:',pre)

E=(5-pre) # Error
print('Error diff from exact value:',E)