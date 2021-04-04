print('hola mundo')
print('Desde jonnathan')
print('Camilo es gay')
print('monogay')

import matplotlib.pyplot as plt
import numpy as np

x = np.array(list(range(0, 10, 1)))

print(x)

y = x**2
print(y)


y_2 = 3*x-2

plt.plot(x,y, color='blue')
plt.plot(x,y_2, color ='yellow', ls=':')

plt.show()