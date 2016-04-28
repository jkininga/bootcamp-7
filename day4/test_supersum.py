'''
Test suite for super_sum.
'''
from unittest  import TestCase
from  super_sum import super_sum


class SuperSumTestCase(TestCase):
	'''
	Test case for super sum.
	'''
	def test_empty_input(self):
		''' Test empty input.'''
		self.assertEqual(0,super_sum())

	def test_sum_of_integers(self):
		''' Test sum of integers'''
		self.assertEqual(super_sum(1,2,3), 6)
		self.assertEqual(super_sum(-1,1),0)
		self.assertEqual(super_sum(10,20,30),60)
	def test_string_input_returns(self):
		self.assertEqual(super_sum('string',1,4),0)
		
	def test_sum_of_items_in_one_list(self):
		'''
		Test sum of items in a single list
		'''
		self.assertEqual(super_sum([1,2,3]),6)

		
		

