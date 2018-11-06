#! /usr/bin/python3
''' function to get the name of the graph and the names of the co-ordinates '''

def title_name():

    ''' Creating the name of the graph '''
    titlename = input('Enter the name of the graph : ')
    while True:
        if titlename == 'q' or titlename =='Q' :
            break
        else :
            #print(titlename.title())
            return titlename.title()
        print('\n')

def x_axis_name():
    ''' creating the name of the x_co-ordinate '''
    x_axis = input("Enter the name of the x-axis co-ordinate :")
    while True :
        if x_axis == 'q' or x_axis =='Q' :
            break
        else:
            #print(x_axis.upper())
            return x_axis.upper()
        print('\n')

def y_axis_name():
    y_axis = input('Enter the name of the y-axis co-ordinate :')

    while True :
        if y_axis =='q' or y_axis == 'Q' :
            break
        else :
            #print(y_axis.upper())
            return y_axis.upper()
        print('\n')
