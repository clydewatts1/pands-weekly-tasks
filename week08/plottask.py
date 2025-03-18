#------------------------------------------------------------------------------
# File: plottask.py
# Description: plot a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x)=x3 in the range 0 to 10, on the one set of axes.
# Author: Clyde Watts
# Date: 2025-03-18
# Version: v1.0
#------------------------------------------------------------------------------
# Requirements
#------------------------------------------------------------------------------
#
#"Weekly Task 8
#Write a program called plottask.py that displays:
#
#a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range 0 to 10, 
#on the one set of axes.
#Some marks will be given for making the plot look nice (legend etc).
#
#Please put a copy of the image of the plot (.png file) into the repository
#
#---------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import os


def main():
    # setup variables for normal distribution
    # mmakes it easier to change values
    mean = 5
    standard_deviation = 2
    number_of_values = 1000
    
    # setup 2 sublots for both plots 
    # datacamp course showed how to set style and a few other attributes
    # https://learn.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib
    # make the plot a bit bigger because I have long titles
    fig, ax = plt.subplots(2, 1, figsize=(10, 10))
    fig.suptitle('Histogram of Normal Distribution and Scatter Plot of h(x)=x^3', fontsize=16)
    # Histogram of normal distribution
    ax[0].hist(np.random.normal(mean, standard_deviation, number_of_values), bins=100 \
        , color='blue', label='Normal Distribution')
    ax[0].set_title(f"Histogram of Normal Distribution Mean {mean} and Standard Deviation {standard_deviation}")
    ax[0].legend()
    ax[0].set_xlabel('Value')
    ax[0].set_ylabel('Frequency')
    ax[0].grid(True)
    # Plot of h(x)=x3
    # generate list of x values from 0 to 10
    # picked a step of 0.1 to get a smooth curve
    x = np.arange(0,10,0.1)
    # y values are x cubed
    y = x**3
    # assume that we want to plot a scatter plot
    ax[1].plot(x, y, color='orange', label='h(x)=x^3')
    ax[1].set_title('Plot of h(x)=x^3')
    ax[1].legend()
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('h(x)')
    ax[1].grid(True)

    #plt.show()
    # save the plot
    # get directory of python script
    # saves me copying the file to the correct directory
    # __file__ is "this" python script
    # realpath gets the full path of the file
    # dirname gets the directory of the file
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # save the plot in the same directory as the script
    plt.savefig(f'{dir_path}/plottask.png')


if __name__ == "__main__":
    main()