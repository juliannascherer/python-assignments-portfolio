import numpy as np
import matplotlib.pyplot as plt

def normal_density (mean, variance, x):
    normal_distribution = (1 / ((2*np.pi*variance)**0.5)) * (np.exp((-(x-mean)**2)/(2*(variance))))
    return normal_distribution

#first plot
x_value = np.linspace (-10,10,500)
y1 = normal_density(0,1,x_value)
plt.plot (x_value,y1, label = "f(x1)")

#second plot
y2 = normal_density(0,5,x_value)
plt.plot (x_value,y2, label = "f(x2)")

#third plot
y3 = normal_density(0,0.5,x_value)
plt.plot (x_value,y3, label = "f(x3)")
plt.title ("Normal Density Function")
plt.xlabel ("x")
plt.ylabel ("Density")
plt.legend ()
plt.show ()

def integration (mean, variance, a, b):
    n = 1000

    w = (b-a)/n
    midpoint = np.linspace (a + (w/2), b - (w/2), n)
    y = normal_density(mean, variance, midpoint)

    normal_distribution_integral = np.sum (y*w)
    return normal_distribution_integral

average_height = 171
average_height_variance = 7.1**2
a = 162
b = 190

print ("The probability that a randomly chosen man has a height between", a, "and", b, "is", integration(average_height,average_height_variance,a,b))


#-----------Question 4-----------------
def average_dosage (mean, variance, a, b):
    n = 1000
    dosage = lambda x: 2.38 * x**2  #D(x) = 2.38X^2
    w = (b-a)/n
    midpoint = np.linspace(a + (w/2), b - (w/2), n)
    y = normal_density(mean, variance, midpoint)
    dosage = dosage (midpoint)
    expected_dosage = np.sum (dosage*y*w)
    return expected_dosage

print ("The estimated average dosage is", average_dosage(average_height,average_height_variance,a,b))

