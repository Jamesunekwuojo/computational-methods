def function(x, y):
    return 3 * x * x * y


def runge_kutta(x0, y, x, h):
    while x0 < x:
        
        k1 = function(x0, y)
        
        xk = x0 + 0.5 * h
        yk2 = y + 0.5 * h * k1
        k2 = function(xk, yk2) 
        
        yk3 = y + 0.5 * k2
        k3 = function(xk, yk3) 
        
        xk4 = x0 + h
        yk4 = y + h * k3
        k4 = function(xk4, yk4)
        
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        
        x0 = x0 + h
        
        print(f"The value of y at x = {x0:.1f} is {y:.8f}") 
        print("") 
        # print("The value of y at x is: ","%.1f"%x0, " is ", "%.8f"%y)
        """
        print(
            "%.1f" % x0,
            " | ",
            "%.8f" % k1,
            " | ",
            "%.8f" % k2,
            " | ",
            "%.8f" % k3,
            " | ",
            "%.8f" % k4,
            " | ",
            "%.8f" % y,
        )
        """


x0 = 0
y = 1
x = 1
h = 0.1

runge_kutta(x0, y, x, h)