def function(x, y):
    return 3*x*x*y

def rungekutta_2stage(x0,  y, a, h, x):
    
    while x0<x:
        
        k1 = function(x0, y)
        
        c1 = h * (1 - 1/2*a)
        c2 = h * 1/2*a
        
        xk2 = x0 + a * h
        
        yk2 = y + a * k1
        
        k2 = function(xk2, yk2)
        
        y = y + c1 * k1 + c2 * k2
        
   
        
        x0 = x0 + h
        
        print(f"The value of y at x = {x0:.1f} is {y:.8f}")  
        print("")
        
# Initial conditions
x0 = 0
y = 1
x = 1
h = 0.1

rungekutta_2stage(x0, y, 1/2, h, x)
# The value of y at x = 0.1 is 1.015
#