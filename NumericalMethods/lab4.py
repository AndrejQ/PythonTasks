from matplotlib.pyplot import plot,show
from numpy import linspace

N=5
a=-1
b=1
L=(b-a)/N
split=25

xi=[]
for i in range(N+1):
    xi.append(a+i*L)

def spline(xi,xinext,f,fnext,m,mnext,x):
    global L
    return ((xinext-x)**2*(2*(x-xi)+L)*f)/(L**3)\
           +((x-xi)**2*(2*(xinext-x)+L)*fnext)/(L**3)\
           +((xinext-x)**2*(x-xi)*m)/(L**2)\
           +((x-xi)**2*(x-xinext)*mnext)/(L**2)

def function(x):
    return 1/(1+25*(x**2))

def derivate(i):
    global xi
    global L
    global N
    if i == 0:
        return (-3*function(xi[0])+4*function(xi[1])-function(xi[2]))/(2*L)
    elif i == N:
        return (3*function(xi[N])-4*function(xi[N-1])+function(xi[N-2]))/(2*L)
    else:
        return (function(xi[i+1])-function(xi[i-1]))/(2*L)

def sum():
    global xi
    global L
    global N
    global split
    sum=[]
    for i in range(N):
        xi1 = linspace(xi[i], xi[i+1], split)
        sum += [spline(xi[i],xi[i+1],function(xi[i]),function(xi[i+1]),derivate(i),derivate(i+1),x) for x in xi1]
    return sum

x = linspace(-1,1,split*N)
plot(x,function(x),x,sum(),'--r', linewidth = 2)
show()