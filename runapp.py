#! /usr/bin/python3
import matplotlib.pyplot as plt
from value import get_x_axis ,get_y_axis
from titles import title_name , x_axis_name,y_axis_name

def graph():
    ''' This plots the graph ,different graphs can be plotted by the user until otherwise stated'''

    print('\t\t\t******************************************')
    print("\t\t\t  Welcome ,this is a graph plotting app")
    print('\t\t\t******************************************')

    while True :
        print("Enter the following items")
        plt.title(title_name() , fontsize=18)
        plt.xlabel(x_axis_name() , fontsize=12)
        plt.ylabel(y_axis_name (), fontsize=12)

        plt.plot(get_x_axis() , get_y_axis() , linewidth = 5)

        plt.show()
        plt.savefig(name = input("Name of the graph : "))

        print('Would you like to plot a new graph (y or n)')
        repeat = input()

        if repeat == 'y' or repeat == 'Y': # if answer is yes , program re-runs
            continue
            print('\n')
        elif repeat == 'n' or repeat == 'N': # else if no ,program is stop
            break
        else : # and if answer is not either (y / n) error is passed and quit function is re-run
            pass # pass without producing an error message


graph() # function call for running the program
