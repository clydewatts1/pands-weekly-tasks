#------------------------------------------------------------------------------
# File:    collatz.py
# Author:  Clyde Watts
# Date:    2025-02-18
#------------------------------------------------------------------------------
# Requirements:
# -------------
# Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.
#
#At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#
#Have the program end if the current value is one.
#
#Push the program in your pands-weekly-tasks GitHub repository (like you do for all the weekly tasks).

#Example of it running:
#
#$ python collatz.py
#
#Please enter a positive integer: 10
#
#10 5 16 8 4 2 1

#--------------------------------------------------------------------------------
# Function: read_positive_integer() -> int
#--------------------------------------------------------------------------------
def read_positive_integer() -> int:
    """
        Prompt the user and read a positive integer.
        
        The assumption is that a valid integer is a positive number.
        Empty input is used for quitting.
        Will repeat until a valid integer is entered or an empty string is entered.
        
        Returns:
            int: The positive integer entered by the user or None if an empty string is entered.
        
        Note:
            Invalid input will re-prompt the user.

    """
    # initialise positive integer to None - no positive integer entered
    positive_integer = None
    while True:
        # Prompt the user and read in the positive integer
        positive_integer = input("Please enter a positive integer: ")
        # check if empty string entered
        if len(positive_integer) == 0:
            positive_integer = None
            print("Quit: Empty String entered")
            break
        # check if input is a positive integer
        try:
            positive_integer = int(positive_integer)
            if positive_integer <= 0:
                print("Try again: Please enter a positive integer")
                continue
            break
        except ValueError:
            print("Invalid input: Please enter a positive integer")
    return positive_integer

#--------------------------------------------------------------------------------
# Function: collatz_conversion(i int) -> list
#--------------------------------------------------------------------------------
def collatz_conversion(work_integer):
    """
    Perform the Collatz conversion on a given integer.

    The Collatz conjecture is a sequence defined as follows:
    - Start with any positive integer.
    - If the integer is even, divide it by 2.
    - If the integer is odd, multiply it by 3 and add 1.
    - Repeat the process until the integer becomes 1.

    This function generates the Collatz sequence for a given integer and returns it as a space-separated string.

    Parameters:
    work_integer (int): The starting integer for the Collatz sequence.

    Returns:
    str: A space-separated string representing the Collatz sequence.
    """

    # initialise result list to first value
    result_list = [str(work_integer),]
    # Loop until kick out clause work_integer = 1 
    while work_integer != 1:
        # if even
        if work_integer % 2 == 0:
            # div 2 - keep as integer , there should be no remainder because of mod 2
            work_integer //= 2
        else:
            # multiply by 3 and add 1 - becomes even next iteration
            work_integer = work_integer * 3 + 1
        # append to list
        result_list.append(str(work_integer))
    return(' '.join((result_list)))
#--------------------------------------------------------------------------------
# Function: collatz() -> None
#--------------------------------------------------------------------------------
def collatz() -> None:
    """
        Calculate the Collatz sequence for a positive integer.
        
        The assumption is that a valid integer is a positive number.
        Empty input is used for quitting.
        Will repeat until a valid integer is entered or an empty string is entered.
        
        Returns:
            None
        
        Note:
            Invalid input will re-prompt the user.

    """
    # read in a positive integer
    postive_integer = read_positive_integer()
    # None entered - exit
    if postive_integer == None:
        return
    collatz_list = collatz_conversion(postive_integer)
    print(collatz_list)

    

if __name__ == "__main__":
    # call function which does the majik
    collatz()