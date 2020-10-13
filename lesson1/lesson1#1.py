print('hi')
import numpy as np
#x=[1,10,1000]
x=input('enter x: ')
x=int(x)
print(x)
for i in [1,2,3]:
    y=np.log((1/(np.e**np.sin(x)+1)/(5/4)+(1/x**15)))/(np.log(1+x**2))
print(y)
