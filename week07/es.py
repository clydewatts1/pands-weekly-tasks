#------------------------------------------------------------------------------
# File: es.py
# Description: A program that reads in a text file and outputs the number of e's it contains.
# Author: Clyde Watts
# Date: 2025-03-12
# Version: v1.0
#------------------------------------------------------------------------------
# Requirements
#------------------------------------------------------------------------------
#Write a program that reads in a text file and outputs the number of e's it contains.
# # Think about what is being asked here, document any assumptions you are making.
#
#The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.
#
#Marks will be given for dealing with errors eg no argument, filename that does not exist, or is not a text file.
#
#
#
#$ python es.py moby-dick.txt
#---------------------------------------------------------------------------------
# Assumptions
# 1. That there can be one ore more txt files
# 2. All files are <filename>.txt -- requirement txt files
# 3. File opened as utf-8
# 4. Assume NO-BOM
# 5. Assume only lower case e - did not specify upper case
# Abend Conditions
# 1. No file as arguments
# 2. Invalid File or open error
# 3. Not a file with type txt

#116960
import os
import sys

# Things to count
CHARACTERS_TO_COUNT = 'e'
ENCODING = 'utf-8'

def help_msg():
    """
    Prints a help message for the script usage.

    The help message provides information on how to use the script, specifying that
    the script expects one or more text files with the extension .txt as arguments.

    Usage:
        es.py <text files>
        where <text files> is one or more text files with name <name>.txt
    """
    print("""HELP:\nes.py <text files>\n   where <text files> is one or more text files with name <name>.txt\n""")

def error_msg(msg):
    """
    Prints an error message and a help message.

    Args:
        msg (str): The error message to be displayed.

    Returns:
        None
    """
    print(f"""ERROR: {msg}\n program will abend\n""")
    help_msg()

def main():
    # check that args is great than 2 ( command plus at least one parameter)
    if len(sys.argv) <= 1:
        error_msg("No text file argument")
        exit(1)
    # now check that files exist before processing
    for file in sys.argv[1:]:
        # check if file exists
        if not os.path.isfile(file):
            error_msg("File {} does not exist".format(file))
            exit(2)
        # check if file is a text file
        if not file.endswith(".txt"):
            error_msg("File {} is not a text file".format(file))
            exit(3)
        # open file and read it
        try:
            with open(file,"r",encoding=ENCODING) as fh:
                txt = fh.read()
                # count the number of e's in the text
                character_count = txt.count(CHARACTERS_TO_COUNT)
            print(f"File {file} has {character_count} {CHARACTERS_TO_COUNT}'s")
        except Exception as e:
            error_msg("Error opening file {}: {}".format(file,e))
            exit(4)
    


# -----------------------------------------------------------------------------
# Run the main function
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()