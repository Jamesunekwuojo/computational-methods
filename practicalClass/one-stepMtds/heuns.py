def function(x, y):
    return 3*x*x*y

def heun(x0, y, h, x):
    while x0<x:
        
        k1 = function(x0, y)
        
        xk2 = x0 + (2/3) * h
        yk2 = y + (2/3) * h * k1
        
        y = y + (h/4) * (k1 + 3 * function(xk2, yk2))
        
        x0 = x0 + h
        
        print(f"The value of y at x = {x0:.1f} is {y:.8f}")  
        print("")
        
# Initial conditions
x0 = 0
y = 1
x = 1
h = 0.1

heun(x0, y, h, x)