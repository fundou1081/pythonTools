import numpy as np
import pylab as pl

x=np.linspace(-1,1,100)
y=np.linspace(-1,1,100)
[x,y]=np.meshgrid(x,y)

U=1/np.sqrt(x**2+y**2)
[EX,EY]=np.gradient(-U)

pl.streamplot(x,y,EY,EX)
pl.show()