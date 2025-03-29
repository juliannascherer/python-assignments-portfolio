import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#exercise a
x, y = sp.symbols('x y')

def question_1 ():
    f = sp.exp(x) * sp.sin(y) + y**3

    df_dx = sp.diff(f, x)
    df_dy = sp.diff(f, y)
    return df_dx, df_dy

print ("Exercise a:", question_1())


#exercise b
def question_2 (x_value,y_value):
    g = (x**2)*y + x * (y**2)
    gradient_vector_x = sp.diff(g,x)
    gradient_vector_y = sp.diff(g,y)
    gradient_vector_magnitude = (gradient_vector_x**2 + gradient_vector_y**2)**0.5
    result = gradient_vector_magnitude.subs({x: x_value, y: y_value}).evalf()
    return result

print ("\nExercise b:", question_2(1,-1))


#exercise c
def question_3 ():
    h = sp.ln (x**2 + y**2)

    dh_dx = sp.diff(h,x)
    dh_dy = sp.diff(h,y)

    d2h_d2x = sp.diff(dh_dx,x)
    d2h_d2y = sp.diff(dh_dy,y)
    d2h_dxy = sp.diff(dh_dx,y)
    d2h_dyx = sp.diff(dh_dy,x)

    return dh_dx, dh_dy, d2h_d2x, d2h_d2y, d2h_dxy, d2h_dyx

one, two, three, four, five, six = question_3()

print ("\nExercise c:")
print ("dh_dx =", one)
print ("dh_dy =", two)
print ("d2h_d2x =", three)
print ("d2h_d2y =", four)
print ("d2h_dxy =", five)
print ("d2h_dyx =", six)

def question_4 ():
    j = x ** 3 - 3 * x * y + y ** 3
    j_func = sp.lambdify((x, y), j, 'numpy')

    x_vals = np.linspace(-3, 3, 400)
    y_vals = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = j_func(X, Y)

    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.title('Contour plot of $j(x, y) = x^3 - 3xy + y^3$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

calling_Q4 = question_4()
print ("\nFunction for exercise d: x^3 - 3xy + y^3")


def question_5 ():
    j = sp.sin(x**2) + sp.cos(y**2) + (x**2)**3
    j_func = sp.lambdify((x, y), j, 'numpy')

    x_vals = np.linspace(-3, 3, 400)
    y_vals = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = j_func(X, Y)

    plt.contourf(X, Y, Z, levels=50, cmap='viridis')
    plt.colorbar()
    plt.title('Contour plot of $j(x, y) = sin(x^2) + cos(y^2) + (x^2)^3$')
    plt.xlabel('$x$')
    plt.ylabel('$y$')
    plt.show()

calling_Q5 = question_5()
print ("\nFunction for exercise e: sin(x^2) + cos(y^2) + (x^2)^3")
