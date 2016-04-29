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

P1=Person('caro',70)
P2=Person('steve',60)
P3=Person('jane',70)
print P1.say_hello()

print P3.people_count
