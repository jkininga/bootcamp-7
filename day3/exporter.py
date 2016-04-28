#global var / not good practice
people = [('joe', 78),('janet', 90),('brian', 67)]

def super_sum(**arg):
	return sum(args)
def hello_again(name,age):
	return 'i am {} and {} years old'. format(name,age)

def max_min(A):
	'''
	returns max value-min value
	eg [10,20,-5,6,50,8]
	'''
	#return max(A)-min(A)
	max_,min_= A[0], A[0]
	for i in A:
		if i>A[0]> max_:
			max_=i
		if i< min_:
		    min_=i	

	return max_- min_
print max_min([8,6,7,2])		    


