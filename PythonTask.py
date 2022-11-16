import numpy as np                 # Making a 2D Array using NumPy
x=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(x)

from matplotlib import pyplot as plt #Using matplotlib (which works same as matlab in python) to make the plottings
plt.plot([1,2,3],[4,5,1])
plt.show()

import matplotlib.pyplot as pzt   # Code with plottings
x=[1,2,3,4,5]
y=[1,4,9,16,20]
pzt.plot(x,y,'ro')           # ro is used for red circle 
pzt.axis([0,6,0,20])
pzt.show()

import matplotlib.pyplot as pzt    # Same code but this time with proper graph
x=[1,2,3,4,5]
y=[1,4,9,16,20]
pzt.plot(x,y)
pzt.axis([0,6,0,20])
pzt.show()

import numpy as nt               # Making of sin graph using both numpy and matplotlib
from matplotlib import pyplot as plz
fig=plz.figure()
ax=plz.axes()
x=np.linspace(0,10,1000)
ax.plot(x,np.sin(x))
plz.show()