import numpy as np

def npSum():
    a=np.array([0,1,2,3,4])
    b=np.array([9,8,7,6,5])

    c=a**2+b**3
    print(a.ndim, a.shape, a.size, a.dtype, a.itemsize)
    return c

def npFunctions():
    a=np.arange(10,20)
    b=np.ones([3,4])
    c=np.zeros([4,3])
    d=np.full((5,5),99)
    e=np.eye(6)
    print(a,b,c,d,e)

def npFunctionPart2():
    a=np.array([[1,2,3,4],[3,4,5,6],[6,7,7,8]])
    b=np.array([[0,2,3,4],[0,4,5,6],[0,7,7,8]])
    c=np.ones_like(b)
    d=np.zeros_like(b)
    e=np.full_like(b,999)
    f=np.linspace(10,100,5)
    g=np.concatenate([a,b])
    print(a,b,c,d,e,f,g)

def npFunctionsPart3():
    print("\nIn npFunctionPart3\n")
    a=np.array([[1,2,3,4],[3,4,5,6],[6,7,7,8]],dtype=np.int32)
    a=a.astype(np.float)
    print(a.shape)
    b=a.reshape((4,3))
    print(b,b.shape)
    c=a.flatten()
    print(a,c)

def npFunctionPart4():
    a=np.arange(-10,100)
    b=np.abs(a)
    c=np.sqrt(b)
    d=np.square(a)
    e=np.log(b)
    f=np.exp(a)
    g=np.sign(a)
    print(a,b,c,d,e,f,g)

    na= g*9
    axy=a.shape
#    ax=axy[0]
#    ay=axy[1]
    print(axy)



if __name__ == '__main__': # when run as a script
    print(npSum())
    npFunctions()
    npFunctionPart2()
    npFunctionsPart3()
    npFunctionPart4()