import numpy as np

def function(x, y):
    return -y

def predictorcorrector(x0, y0, h, x):
    
    n = int((x-x0)/h)
    
    n_value = 0
    
    x = np.linspace(x0, x, n+1)
    y = np.zeros(n+1)
    y[0] = y0
    
    #eluers method
    y[1] = y[0] + h*function(x[0], y[0])
    print(f"The initial conditions are n={n_value}, x = {x[n_value]}, y = {y[n_value]}")
    print("")
    
    
    for i in range(1, n):
        
        y_predictor = y[i] + (h/2) * (3*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        print(f"The predictor value at x = {'%.1f'%x[i]} is {'%.10f'%y_predictor}")
        print("")
        
        y_corrector = y[i+1] + (h/12) * (5*function(x[i+1], y_predictor) + 8*function(x[i], y[i]) - function(x[i-1], y[i-1]))
        print(f"The corrector value at x = {'%.1f'%x[i]} is {'%.10f'%y_corrector}")
        print("")
        
        y[i+1] = y_corrector
        
        n_value += 1
        print(f"The value of n is {n_value}, x = {'%.1f'%x[n_value]}, y = {'%.10f'%y[n_value]}")
        print("")
        
    return x, y

x0 = 0
y0 = 1
h = 0.001
x = 1

x, y = predictorcorrector(x0, y0, h, x)
