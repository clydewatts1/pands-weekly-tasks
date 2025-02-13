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
def read_account_number(min_length = 1,max_length = 16) -> str:
    """
        Prompt the user and read a 1-16 digit account number.
        
        The assumption is that a valid account number is between 1 and 16 digits.
        Credit cards are 16 digits long - need a rule.
        Empty input is used for quitting.
        Will repeat until a valid account number is entered or an empty string is entered.
        
        Args:
            min_length (int): Minimum length of the account number.
            max_length (int): Maximum length of the account number.
        
            str: The account number entered by the user or None if an empty string is entered.
        
        Note:
            If invalid input is entered, the program will abend.

    """
    # compile regex before loop , more efficient
    # number must be between 1 and 16 digits
    # the ^ ( carrot ) means start of string and $ means end of string
    # \d is a number could have put [0=9] but \d is more compact
    # {1,16} means length 1 to 16
    regex_string =f"^\\d{{{min_length},{max_length}}}$"
    regex = re.compile(regex_string)
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
    """
        Read in a 10 digit account number and output the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
        
        The assumption is that the account number is 10 digits long.
        The last 4 digits are displayed and the first 6 digits are replaced with Xs.
        If the account number is less than 10 digits long then the whole account number is displayed.
        If the account number is greater than 10 digits long then the last 4 digits are displayed and the first length - 4 digits are replaced with Xs.
        Empty input is used for quitting.
        
        Note:
            If invalid input is entered, the program will abend.
    """
    # Read in account number from user and console
    # Set the number of characters to display at the end of the account number
    DISPLAY_LAST_N_CHARS = 4
    OBFUSCATE_CHAR = "X"
    account_number = read_account_number()
    # if empty string entered then return
    # means user has quit
    if account_number is None:
        return
    # we want to work out the slice length
    length_account_number = len(account_number)
    # start off with no fill characters
    right_fill_chars = ""
    last_left_chars=account_number
    if length_account_number > DISPLAY_LAST_N_CHARS:
        # get last 4 characters
        last_left_chars = account_number[-DISPLAY_LAST_N_CHARS:]
        # fill with X the first length - DISPLAY_LAST_N_CHARS characters
        right_fill_chars = OBFUSCATE_CHAR * (length_account_number - DISPLAY_LAST_N_CHARS)
    
    # print out obfuscated account number
    print(f"The account number is: {right_fill_chars}{last_left_chars}\n")





if __name__ == "__main__":
    main()