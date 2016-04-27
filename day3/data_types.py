def data_type(x):
    """
    Takes in an argument x:
            - For an integer , return x ** 2
            - For a float, return x/2
            - For a string, returns "hello" + x
            - For a boolean, return "boolean"
            - For a long, return squaroot of x
    """
    if type(x) == int:
        return x ** 2

    elif type(x) == float:
        return x / 2

    elif type(x) == str:
        return "Hello  {}".format(x)

    elif type(x) == bool:
        return "boolean"

    elif type(x) == long:
        return "long"

    else:
        return "That'a not a python primitive data type"
print data_type(8)
print data_type(2.7)
print data_type(True)
print data_type(6666666666666666666666666678998676755)
print data_type('MOTHER')





	
	  
	 