import numpy as np
import math
ba=np.array([34,108,64,88,99,51])
ta=np.array([5,17,11,8,14,5])

sum_xy=np.sum(ba*ta)
sum_x=np.sum(ba)
sum_y=np.sum(ta)
n=len(ba)
N=(n*sum_xy-(sum_x*sum_y))

sum_sq_x= np.sum((ba*ba))
Sum_whole_sq_x=(sum_x*sum_x)
cx=(n*sum_sq_x)-Sum_whole_sq_x

sum_sq_y= np.sum((ta*ta))
Sum_whole_sq_y=(sum_y*sum_y)
cy=(n*sum_sq_y)-Sum_whole_sq_y

D=math.sqrt(cx*cy)
cr=N/D
print('Correlation Coefficient value:',cr)