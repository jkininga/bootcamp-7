def super_sum(*args):
	'''
	Returns a sum of numbers.
	e.g
	    super_sum()==>'Test Case for super sum'
	    super_sum(1,2,3)==> 6
	    super_sum([1,2,3])==> 6
	    super_sum('string', 2,3)==> 0

	    super_sum([10],[20,30])==> 60
	'''
	total = 0
	if args:
		for x in args:
			if type(x) == list:
				total += sum(x)
			elif type(x)== str:
				return 0
			else:
				total += x
		return total		
	else:
		return 0
print super_sum([2,4],[7,9,6],[3,2])		

		

		
	
	

