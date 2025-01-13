from BivarientLinearRegression_Model import LinearRegression
x=[34,108,64,88,99,51]
y=[5,17,11,8,14,5]
model=LinearRegression()
model.fit(x,y)
print('Intercept:',model.I)
print('Slope:',model.S)

res=model.predict(550)
print('Predicted Value:',res)