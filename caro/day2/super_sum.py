def super_sum(A):
	'''
	    Takes a list A, and and: 
	        -Halves every even number 
	        -Doubles every odd number
	    And returns the sum of all.
	'''
	total = 0
	for i in A:
		if i % 2 == 0:
			 total +=(i / 2)
		else:
		    total +=(i * 2)
	return total

	
	
print(super_sum([2,3]))		