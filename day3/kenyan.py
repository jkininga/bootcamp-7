from person import Person
class Kenyan(Person):
	def probe(self, corrupt):
		self.corrupt=corrupt
	def is_corrupt(self):
		if self.corrupt:
			return "Yes"
		return "No"	



k=Kenyan('aniota', 50)
k.probe(True)
print 'is {} corrupt? {}'.format(k.name,k.is_corrupt())
print k.say_hello()

		