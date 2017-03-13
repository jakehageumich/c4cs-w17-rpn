import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		#print("add result: " + str(result))
		#print("rpn.calculate(1 1 +): " + str(rpn.calculate("1 1 +")))
		self.assertEqual(2, int(result))
		print("Passed add")
	def test_subtract(self):
		result = rpn.calculate("2 4 -")
		self.assertEqual(-6, result)
		print("Passed subtract")
	def test_multiply(self):
		result = rpn.calculate("3 5 6 *")
		self.assertEqual(90, result)
		print("Passed multiply")
	def test_divide(self):
		result = rpn.calculate("4 8 /")
		self.assertEqual(2, result)
		print("Passed divide")
