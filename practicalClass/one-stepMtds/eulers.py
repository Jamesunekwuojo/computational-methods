def function(x,y):
    return 3*x*x*y

def euler(x0, y, h, x):
    while x0 < x:
        
        y = y+h*function(x0, y)#euler method formula
        
        x0 = x0+h
        
        print("The Approximate solution of y at x", '%.1f'%x0 ,"---> ","%.8f"%y )
        print("")
    
x0 = 0
x = 1
h = 0.1
y = 1
euler(x0, y, h, x)