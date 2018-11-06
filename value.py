#! /usr/bin/python3


''' These functions are used to get the values of the x-axis and y-axis co-ordinate ,
 	the values are gotten from the user and then appended to an empty list which serves as the holder of the co-ordinate values , the input end s whith a sentinel value of -0
	NOTE : all values are represented in floating point data type '''


def get_x_axis() :
	'''function for the x_axis co-ordinates '''
	x_axis = []
	print('Enter your x-axis values "use (0) to end input" : ')
	while True :
		try :# Testing the input to see if it is a number
			xaxis = float(input())
			if xaxis == -0 :
				break
		except ValueError :
			pass# if input in not a number it passes it and does not create any error messsage

		else :# creates the list for the co-ordinates
			x_axis.append(xaxis)

	print(x_axis)
	return x_axis

def get_y_axis() :
	'''function for the y_axis co-ordinates '''
	y_axis = []
	print('Enter your y-axis values"use (0) to end input"  : \n')
	while True :
		# Testing the input to see if it is a number
		try :
			yaxis = float(input())
			if yaxis == -0 :
				break
		except ValueError :
			pass # if input in not a number it passes it and does not create any error messsage
		else :
			# creates the list for the co-ordinates
			y_axis.append(yaxis)

	print(y_axis)
	return y_axis
