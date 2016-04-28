class Person(object):
	people_count = 0

	def __init__(self, name, age=0):
		self.name = name
		self.age = age
		Person.people_count +=1

	def __repr__(self):	
		return "<{},{}>".format(self.name,self.age)


	def say_hello(self):
		return "hello, i'm {} and {} y/o".format(self.name,self.age)