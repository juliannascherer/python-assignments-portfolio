#importing necessary packages for the question
import matplotlib.pyplot as plt
import numpy as np

#defining the gradient descent function
#the function, learning rate, and inital point are inputted into this
def gradient_descent (f, learning_rate, inital_point, tolerance = 1e-6, max_steps = 1000):

    #function for the derivative of the function evaluated at the 'base_point'
    def deriv (f, base_point):
        #estimated derivative at base_point using the symmetric approx
        return (f(base_point + 10 ** (-10)) - f(base_point - 10 ** (-10))) / (2*10**(-9))

    x_coords = [inital_point] #stores the x values
    y_coords = [f(inital_point)] #stores the y values

    #looping through all max step values, max step is defined in the gradient_descent function
    for i in range (max_steps):
        current_x = x_coords[-1] #using the previous x coordinate as the current x value
        gradient = deriv(f, current_x) #taking the derivative

        #condition to check if the absolute gradient value is smaller than the tolerance
        #if yes, it will break out of the loop
        if abs (gradient) < tolerance:
            break

        #using the learning rate and gradient to determine the x value used in the next iteration
        next_x = current_x - learning_rate * gradient
        x_coords.append(next_x) #appending the next x value to the list of x coordinates
        y_coords.append(f(next_x)) #appending the next y value to the list of y coordinates

    #the most recent iteration of x and y coordinates will be outputted
    return x_coords, y_coords

#defining the given functions in the question
def f1 (x):
    return x**2

def f2 (x):
    return 2*x**4 - 3*x**2 + 2*x-1

def funny_function(x):
    if x>0:
        return x**x
    elif x==0:
        return 1
    else:
        return abs(x)**abs(x)

def f4 (x):
    return np.abs(x)

all_functions = [f1, f2, funny_function, f4] #adding the functions to a list
learning_rates = [0.01, 0.01, 0.01, 0.01] #setting the learning rate value
initial_points = [0.1, 0.2, 0.6, 0.5] #setting the inital point value

#loop running through the functions in the list and applying their set learning rate and inital point
for i, func in enumerate(all_functions):
    x_coords, y_coords = gradient_descent(func, learning_rates[i], initial_points[i])
    plt.figure(i + 1) #for each function to go on its own graph
    plot_range = np.linspace(min(x_coords) - 0.5, max(x_coords) + 0.5, 10000)
    function_range = [func(i) for i in plot_range]

    #plotting each of the functions
    plt.plot(plot_range, function_range, label=f'Function {i + 1}')
    plt.plot(x_coords, y_coords, color='red', label='Descent Path')
    plt.title(f'Gradient Descent on Function {i + 1}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid()

    #printing out the determined minima for each function
    print(f"Function {i+1}: Final point: x = {round(x_coords[-1], 3)}, y = {round(y_coords[-1], 3)}")

plt.show()

#the gradient descent to find the local minimum of |x| should not work because the derivative is undefined