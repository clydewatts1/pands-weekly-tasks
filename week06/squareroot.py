#------------------------------------------------------------------------------
# File:    squareroot.py
# Author:  Clyde Watts
# Date:    2025-02-24
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Requirements:
# -----------------------------------------------------------------------------
#Weekly task 6
#Write a program that takes a positive floating-point number as input 
#and outputs an approximation of its square root.
#You should create a function called <tt>sqrt</tt> that does this.
#I am asking you to create your own sqrt function and not 
#to use the built in functions x ** .5 or math.sqrt(x).
#This is to demonstrate that you can research and 
#code a process (If you really needed the square root you would use one of the above methods). 
#I suggest that you look at the newton method at estimating square roots. 
#This is a more difficult task than some of the others, but will be marked equally, 
#so only do as much work on this as you feel comfortable.
#------------------------------------------------------------------------------
# Function : sqrt_tailor_method
# -----------------------------------------------------------------------------
def sqrt_tailor_method(n, threshold=0.000000001, max_iterations=100):
    """
    Calculate the square root of a number using the Taylor series method.
    Parameters:
    n (float): The number to find the square root of.
    threshold (float): The error threshold for the approximation. Default is 0.000000001.
    max_iterations (int): The maximum number of iterations to perform. Default is 1000.
    Returns:
    float: The approximated square root of the number.
    """
    # TODO : Implement the Taylor series method to calculate the square root of a number
    #       using the given threshold and maximum number of iterations.
    
    # initial x
    x = 1.0
    # this is needed for calculating the square 
    # bumped up ( x - 1.0 ) each time
    minus_n = n - 1.0
    square_minus_n = 1.0
    # 2 * i
    two_i = -1
    # loop 1000 times to get the square root
    square_root = 1.0
    # loop 1000 times to get the square root
    for i in range(max_iterations):
        # need this for validate the square
        square = x * x
        # calculate next square root
        square_minus_n *= minus_n
        # calculate two_i
        two_i *= -2
        # calculate the next x
        x += square_minus_n / two_i
        # if there is a "error" of less than 0.000001, kick out of the loop
        if abs(square - n) < threshold:
            break
         

    return x
# -----------------------------------------------------------------------------
# Function : sqrt_newton_method
#  Using newton method at estimating square roots.
# -----------------------------------------------------------------------------
# Define a constant for the threshold value
THRESHOLD = 0.000000001

def sqrt_newton_method(n, threshold=THRESHOLD, max_iterations=1000):
    """
    Calculate the square root of a number using the Newton-Raphson method.
    Parameters:
    n (float): The number to find the square root of.
    threshold (float): The error threshold for the approximation. Default is THRESHOLD.
    max_iterations (int): The maximum number of iterations to perform. Default is 1000.
    Returns:
    float: The approximated square root of the number.
    """

    # using the newton method
    # x = x - (x^2 - n) / (2 * x)
    if n < 2.0:
        x = n
    else:
        x = n / 2.0
    # loop 1000 times to get the square root
    for i in range(max_iterations):
        # calculate the square of x
        # need to use the square two times , so store it in a variable
        square = x * x
        # if there is a "error" of less than 0.000001, kick out of the loop
        if abs(square - n) < threshold:
            break
        # Calculate the new x value
        x = x - (square - n) / (2.0 * x)
    return x

# -----------------------------------------------------------------------------
# Function : enter_floating_point_number
# -----------------------------------------------------------------------------
def enter_floating_point_number(message):
    """
    Prompts the user to enter a floating-point number with a custom message.

    Args:
        message (str): The message to display when prompting the user for input.

    Returns:
        float: The valid positive floating-point number entered by the user.

    Raises:
        SystemExit: If the user enters an invalid value or a negative number.
    """
    try:
        number = float(input(message))
    except ValueError:
        print("ERROR : Please enter a valid floating-point number.")
    if number <= 0:
        print("ERROR : Please enter a positive floating-point number.")
        exit(2)
    return number


# -----------------------------------------------------------------------------
# Function : main
# -----------------------------------------------------------------------------
def main():
    """
    Main function to calculate the square root of a positive floating-point number
    entered by the user using the Newton-Raphson method.

    Prompts the user to enter a positive floating-point number, calculates its
    square root using the Newton-Raphson method, and prints the result.

    Functions:
        enter_floating_point_number(prompt: str) -> float: Prompts the user to enter a floating-point number.
        sqrt_newton_method(number: float) -> float: Calculates the square root of a number using the Newton-Raphson method.
    """
    number = enter_floating_point_number("Please enter a positive floating-point number: ")
    square_root = sqrt_newton_method(number)
    print(f"The square root of {number} is approx. {square_root}.")
# -----------------------------------------------------------------------------
# Run the main function
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()


