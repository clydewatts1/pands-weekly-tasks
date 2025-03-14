#------------------------------------------------------------------------------
# File:    bank.py
# Author:  Clyde Watts
# Date:    2025-02-04
#------------------------------------------------------------------------------
# Requirements:
# The program should:
# 
# Prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# $ python bank.py
# Enter amount1(in cent): 65
# Enter amount2(in cent): 180
# The sum of these is €2.45
#--------------------------------------------------------------------------------
# Notes:
# Maybe a bit of an overkill to have a function to read in the amount, but it does make the main function a bit cleaner.
#--------------------------------------------------------------------------------
# import the decimal module
import decimal as d

#--------------------------------------------------------------------------------
# Function: input_amount(prompt_amount_string : str) -> int
#--------------------------------------------------------------------------------
def input_amount(prompt_amount_string : str) -> int:
    """Prompt the user and read in a money amount (in cent)
    Args:
        prompt_amount_string (str): The string to be displayed to the user
    Returns:
        int: The amount entered by the user
    Note: if invalid input is entered the program will abend
    """
    # Prompt the user and read in the amount
    # abend if the user enters a non-numeric value
    # TODO: loop until a valid number is entered
    try:
        amount = int(input(f"Enter {prompt_amount_string}(in cent): "))
        # convert to decimal
        amount = d.Decimal(amount)
    except ValueError:
        print("Error: Please enter a valid number")
        exit(1)
    # Return the amount
    return amount

#--------------------------------------------------------------------------------
# Function: main()
# TODO: Move string generation into file so it is testable - may be overkill
#--------------------------------------------------------------------------------
def main():
    """Add two amounts and print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount"""
    # Call function which prompts the user and reads the 1st amount (in cent)
    amount1 = input_amount("amount1")
    # Call function which prompts the user and reads the 2nd amount (in cent)
    amount2 = input_amount("amount2")
    # Add the two amounts
    total = amount1 + amount2
    # Convert to euro 
    # 100 cent in a euro
    euro = total / d.Decimal(100)
    # format should be EZ9.99
    # Print out the results in wetware readable format
    print(f"The sum of these is €{euro:.2f}") 



# Call the main function
if __name__ == "__main__":
    main()  