def function(x, y):
    return 3 * x * x * y

def modified_euler(x0, y, h, x):
    while x0 < x:
        
        k1 = function(x0, y)
        
        xk2 = x0 + h / 2 
        yk2 = y + (h / 2) * k1  
        
        k2 = function(xk2, yk2)
        
        y = y + h * k2  
        
        print(f"The value of y at x = {x0:.1f} ---> {y:.8f}")  
        print("")
        
        x0 = x0 + h  

# Initial conditions
x0 = 0
y = 1
x = 1
h = 0.1

modified_euler(x0, y, h, x)