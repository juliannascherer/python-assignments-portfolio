import numpy as np
from scipy.special import gamma

#given data
test_scores = [92.64,79.00,84.79,97.41,93.68,65.23,84.50,73.49,73.97,79.11]
national_average = 75
n = len(test_scores)
nu = n - 1
prob = 0.95

def mean_std (test_scores,n):
    # mean
    sum_of_test_scores = 0
    for i in range (len(test_scores)):
        sum_of_test_scores += test_scores[i]
    mean_test_score = sum_of_test_scores/len(test_scores)

    #standard deviation
    standard_dev_sum = 0
    for i in range (n):
        standard_dev_sum += (test_scores[i]-mean_test_score)**2
    standard_deviation = ((1/(n-1))*standard_dev_sum)**0.5

    return mean_test_score, standard_deviation

def finding_to (mean_test_score, standard_deviation, national_average):
    t_o = (mean_test_score - national_average) / (standard_deviation / (n) ** 0.5)
    return t_o

def t_distribution_pdf(x, nu):
    coeff = gamma((nu + 1) / 2) / (np.sqrt(nu * np.pi) * gamma(nu / 2))
    density = coeff * (1 + x**2 / nu) ** (-0.5 * (nu + 1))
    return density

def find_t_star(prob, nu, x_start=0, x_end=20, num_points=10000):
    # Define the x values
    x = np.linspace(x_start, x_end, num_points)
    # Apply the density function to the x values
    y = t_distribution_pdf(x, nu)
    # This next line is the integration
    cdf = np.cumsum(y) * (x[1] - x[0])
    # Find the t-value where the cumulative probability reaches half of the required probability
    target_half_prob = prob / 2
    index = np.where(cdf >= target_half_prob)[0][0]
    return x[index]

#outputting data from the function
mean_test_score, standard_deviation = mean_std(test_scores,n)
print ("The mean test score is:",mean_test_score)
print ("The standard deviation is:",standard_deviation)

t_o = finding_to(mean_test_score, standard_deviation, national_average)
print ("t0 is", t_o)

t_star = find_t_star(prob, nu)
print ("t* is", t_star)


def true_test():
    if -1*t_star <= t_o <= t_star:
        print ("True")
    else:
        print ("False")
true_test()

#Because its false, we reject the null hypothesis. This means that there is a statistically
#significant difference in the test scores of these students compared to the national average.
#Therefore, the teaching technique was beneficial.