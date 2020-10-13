import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
func_=input('give me function: ')
print(func_)
#y= x**2-x-6
y=eval(func_)
with plt.xkcd():
    plt.plot(x, y)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$x$')
    plt.grid(True)
plt.show()
