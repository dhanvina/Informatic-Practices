import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([3,4,0,-1,-3])
c=np.cov(a,b)
print(c)
