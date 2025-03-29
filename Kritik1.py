#this is to have the code loop so the user can keep inputting in values
while 1>0:

    #the user inputs an x value
    inputted_x_value = float (input("\nEnter a value for x: "))

    #function for arctan approximation
    def arctan (inputted_x_value):
        i = 0
        n = 0

        running_arctan_approximation = 0
        #setting the first error value to one so it will enter the loop
        error_value = 1
        approximation_value = 0.0001

        #if the inputted value is within the range
        if 0 <= inputted_x_value<= 1:

            #finding approximation value
            while error_value > approximation_value:

                #approximated value by the polynomial
                numerator_calculation = ((-1) ** i)*(inputted_x_value**((2*i)+1))
                denominator_calculation = (2*i)+1
                calculation = numerator_calculation/denominator_calculation
                running_arctan_approximation = running_arctan_approximation + calculation

                #error calculation
                error_value_numerator = inputted_x_value**((2*n)+1)
                error_value_denominator = (2*n) + 1
                error_value = error_value_numerator/error_value_denominator

                #increasing the counters by one for each iteration of the loop
                i = i + 1
                n = n + 1

            #decreasing the n value by one based on the equation
            n = n-1

            #printed to the screen at the end of the loop
            output_tuple = [running_arctan_approximation, n, error_value]
            return output_tuple

        #if not within the range
        else:
            return "Error!"

    print (arctan(inputted_x_value))