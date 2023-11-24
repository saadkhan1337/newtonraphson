#input:intial x, func(x),derivfunc(x)
#output:root of func()
#calculate krny h values of funk(x) and derivfunc(x) for given initial x
#calculate H: h=func(x)/derivfunc(x) if h is greater than the allowable error e
#h=func(x)/derivfunc(x)
#x=x-h


#finding the root of equation (x**3-x**2+2)
def f(x):
    y=x**3-x**2+2
    return y
def dfdx(x):
    y=3*x*x-2*x
    return y
c=-20
def newtonraphson(x):
       h=f(x)/dfdx(x)
       while abs(h)>=0.001:
          h=f(x)/dfdx(x)
          x=x-h
          print("the root of eq:","%4f"%x)
newtonraphson(c)
















##x=-2
##for i in range(100):
##    xnew= x-(2*x**3-9.5*x+7.51) / (6*x**2-9.5)
##    if abs(xnew-x)<0.001: break
##    x=xnew
##print("the root is %f at %d itegeration:" % (xnew,i))
##









    
    
##def func(x):
##    function=(x*x*x)-(2*x)-1
##    return function
##def derivative(x):
##    h=0.000001
##    derivative=(f(x+h)-f(x))/h
##    return derivaitve
##def newtonraphson(x):
##   return(x-(f(x)/derivative(x)))
##def iterate(p,n):
##    x=0
##    for i in range(n):
##        if i==0:
##            x=newtonraphson(iterate(x,n))
##        else:
##            x=newtonraphson(iterate(x,n))
##        n=n-1
##    reurn x
##print iterate(1,3)
