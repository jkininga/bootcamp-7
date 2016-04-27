def hello(name,age, class_=''):
    '''
    Explains how to pass arguments
    '''
    if class_ != '':
        return "I am {}, {} and {} class".format(name, age, class_)
    return "I am {}, my age is {}".format(name, age)


people = [
            ("Jane", 23, 7),
            ("Joe", 23, 9),
            ("Brian", 23),
            ("Betty", 23),

            ]
for i in people:
    print hello( * i)

def supersum(*args):
	'''
	Takes in variable number of items,
	and returns sum.
	e.g super_sum(10,20) = 30
	    super_sum(10,20,40)=70
	    super_sum(1,4,5,6,7)=23
	'''
	total = 0
	for i in args:
		total += i
	return total	

print supersum(10,20)   
print supersum(1,4,7)
a = [10,40,60]
print supersum(*a)


def hello_again(**kwargs):
	return  "I am {},and i'm {} ".format(kwargs['name'],kwargs['age'])

print hello_again(name='joe', age = 20)
print hello_again(age=20,name='joe')

other_people = [{'name': 'joe', 'age': 98},{'name': 'jane', 'age': 98},{'name': 'peter', 'age': 98}]
joe = {'name' : 'joe', 'age': 98}
print hello_again(**joe)
print hello_again(name='joe', age=98)

for person in other_people:
	hello_again(**person)



 