#------------------------------------------------------------------------------
# File:    weekday.py
# Author:  Clyde Watts
# Date:    2025-02-24
#------------------------------------------------------------------------------
# Requirements:
# -------------
# import data module
from datetime import date

# Requirments
# -------------
# So I can remember them
# Weekly Task 05
# Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)
# 
# You will need to search the web to find how you work out what day it is.
# 
# An example of running this program on a Thursday is given below.
# 
# $ python weekday.py
# Yes, unfortunately today is a weekday.
# 
# 
# An example of running it on a Saturday is as follows:
# 
# $ python weekday.py
# It is the weekend, yay!
# 
# There is no user input.

#------------------------------------------------------------------------------
# Function : weekend_check
#------------------------------------------------------------------------------
def weekend_check(the_date):
    """
    Check if the given date is a weekend or a weekday.
    Parameters:
    the_date (datetime.date): The date to check.
    Returns:
    None: Prints a message indicating whether the date is a weekend or a weekday.
    """

    # isoweekday returns day of the week 1 for monday ... 7 for sunday
    if the_date.isoweekday() >= 6:
        print("It is the weekend, yay!")
    else:
        print("Yes, unfortunately today is a weekday.")
    return

#------------------------------------------------------------------------------
# Function : do_the_date
#------------------------------------------------------------------------------
def do_the_date():
    """
    Get the current date and check if it is a weekday.
    This function retrieves the current date and then calls the 
    `weekend_check` function to determine if the current date 
    falls on a weekend.
    Returns:
        None
    """

    # get the current date
    today = date.today()
    # check if it is a weekday
    weekend_check(today)
    return

#--------------------------------------------------------------------------
# Main
#--------------------------------------------------------------------------
if __name__ == '__main__':
    do_the_date()
    exit(0)

