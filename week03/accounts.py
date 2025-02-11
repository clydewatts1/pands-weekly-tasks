#------------------------------------------------------------------------------
# File:    account.py
# Author:  Clyde Watts
# Date:    2025-02-11
#------------------------------------------------------------------------------
# need re module to use regular expressions to validate input
import re
# Requirements:
# -------------
# The program should:
# 
#Bank account numbers can stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the other other characters replaced with Xs).
#
#Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
#
#$ python accounts.py
#Please enter an 10 digit account number: 1234567890
#XXXXXX7890
#Extra:
#Modify the program to deal with account numbers of any length (yes that is a vague requirement, comment your assumptions)
#--------------------------------------------------------------------------------
# Function: read_account_number() -> str
#--------------------------------------------------------------------------------
def read_account_number() -> str:
    """Prompt the user and read 1-16 digit account number
       The assumption is that that a valid account number is between 1 and 16 digits
       credit cards are 16 digits long - need a rule
       Empty is used for quit input
       Will  repeat until a valid account number is entered or empty string is entered
    Returns:
        str: The account number entered by the user
             or None if empty string entered
    Note: if invalid input is entered the program will abend
    """
    # compile regex before loop , more efficient
    # number must be between 1 and 16 digits
    # the ^ ( carrot ) means start of string and $ means end of string
    # \d is a number could have put [0=9] but \d is more compact
    # {1,16} means length 1 to 16
    regex = re.compile(r"^\d{1,16}$")
    # for 10 digit account number use ^\d{10}$
    # initialise account number to None - no account number entered
    account_number = None
    while True:
        # Prompt the user and read in the account number
        account_number = input("Please enter an account number: ")
        # check if empty string entered
        if len(account_number) == 0:
            account_number = None
            print("Goodbye: Aborted entry")
            break
        # check if valid account number entered
        if regex.match(account_number):
            break
        # invalid account number keyed
        print("Oops: You have made a booboo, please enter a valid account number")
    # Return the account number
    return account_number
    

#--------------------------------------------------------------------------------
# Function: Main
#--------------------------------------------------------------------------------
def main():
    
    account_number = read_account_number()
    if account_number is None:
        return
    # we want to work out the slice length
    length_account_number = len(account_number)
    # start off with no fill characters
    right_fill_chars = ""
    last_left_chars=account_number
    if length_account_number > 4:
        # get last 4 characters
        last_left_chars = account_number[-4:]
        # fill with X the first length - 4 characters
        right_fill_chars = "X" * (length_account_number - 4)
    
    # print out obfuscated account number
    print(f"The account number is: {right_fill_chars}{last_left_chars}\n")





if __name__ == "__main__":
    main()