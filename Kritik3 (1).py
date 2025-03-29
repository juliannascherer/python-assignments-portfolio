import numpy as np

#defining the test functions
#test function i
def f1(x):
    return x**2
#test function ii
def f2(x):
    return np.sin(x)
#test function iii
def f3(x):
    return np.exp(x)
#defining the fixed change in x value
change_in_x = 10 ** -8
def linear_approximation (f, c, E):
    #approximates derivative with central difference method
    derivative = (f(c + change_in_x) - f(c - change_in_x)) / (2 * change_in_x)
    #determining the absolute error between the function and linear approximation
    x1 = c - E
    x2 = c + E
    #linear approximation calculation for x1 and x2 values
    linear_approximation_x1 = f(c) + (derivative * (x1 - c))
    linear_approximation_x2 = f(c) + (derivative * (x2 - c))
    #linear approximation of f(x) around c when x1 < c
    #loop continues until the linear approximation is within the error
    #setting the reasonable number of iteration to be 100 and counted using i and k
    i = 0
    while abs (f(x1) - linear_approximation_x1) > E:
        x1 -= change_in_x
        i = i + 1
        #setting 10 iterations as my reasonable range
        if i >=10:
            return "No such x1 and x2 can be found within a reasonable range"
            break
    #linear approximation of f(x) around c when x2 > c
    #loop continues until the linear approximation is within the error
    k = 0
    while abs (f(x2) - linear_approximation_x2) > E:
        x2 += change_in_x
        k = k + 1
        #setting 10 iterations as my reasonable range
        if k >= 10:
            return "No such x1 and x2 can be found within a reasonable range"
            break
    return float (x1), float (x2)
print (linear_approximation (f1, 1, 0.1))
print (linear_approximation (f2, np.pi/4, 0.05))
print (linear_approximation (f3, 0, 0.01))