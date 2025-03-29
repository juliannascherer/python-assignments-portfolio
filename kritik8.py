import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

#4a
def gradient_descent(x0, y0, f, grad_f, alpha, num_iterations):

    x, y = x0, y0 # Initialize x and y with the initial point
    for i in range(num_iterations):
        # obtain the gradient of f at (x, y)
        grad_x, grad_y = grad_f (x,y)
        # Update x and y by taking a step in the opposite direction of the gradient
        x -= alpha * grad_x
        y -= alpha * grad_y

    return x, y

#4b
def fun_1(x,y):
    return x**2 + y**2

def grad_f_1(x,y):
    grad_x = 2*x
    grad_y = 2*y
    return grad_x, grad_y

test_1 = gradient_descent (0.1,0.1, fun_1, grad_f_1, alpha = 0.1, num_iterations = 10)
print ("test case one (x,y) is:", test_1)
test_2 = gradient_descent (-1,1, fun_1, grad_f_1, alpha = 0.01, num_iterations = 100)
print ("test case two (x,y) is:", test_2)

#4c
def fun_2(x,y):
    return 1-np.exp(-x**2-(y-2)**2)-2*np.exp(-x**2-(y+2)**2)

def grad_f_2(x,y):
    grad_x = (2 * x * np.exp(-x**2-(y-2)**2)) + (4*x*np.exp(-x**2-(y+2)**2))
    grad_y = (2 * (y-2) * np.exp(-x**2-(y-2)**2)) + (4*(y+2)*np.exp(-x**2-(y+2)**2))
    return grad_x, grad_y

test_3 = gradient_descent (0,1, fun_2, grad_f_2, alpha = 0.01, num_iterations = 10000)
print ("test case three (x,y) is:", test_3)
test_4 = gradient_descent (0,-1, fun_2, grad_f_2, alpha = 0.01, num_iterations = 10000)
print ("test case four (x,y) is:", test_4)

X=np.linspace(-5,5,100)
Y=np.linspace(-5,5,100)
x,y=np.meshgrid(X,Y)
z= fun_2 (x,y)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
plt.show ()
#x,y z are variable names.