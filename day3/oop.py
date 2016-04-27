#PEP8
class Person:
	people_count = 0

	def __init__(self, name, age=0):
		self.name = name
		self.age = age
		Person.people_count +=1

	def __repr__(self):	
		return "<{},{}>".format(self.name,self.age)


	def say_hello(self):
		return "hello, i'm {} and {} y/o".format(self.name,self.age)


p1 = Person('joe', 23)
p2 = Person('jane', 23)	
print p1.say_hello()

b=[]
a = [('jane', 23),('joe',50),('jacob',32)]
for name, age in a:
	person= Person(name, age)
	b.append(person)
print b

print Person.people_count
print p2.people_count

for person in b:
	print person.say_hello()

