import unittest
import rpn
class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate("1 1 +")
		self.assertEqual(result, 2)
		print("Passed add: 1 + 1 = " + str(result))
	def test_subtract(self):
		result = rpn.calculate("2 4 -")
		self.assertEqual(-6, result)
		print("Passed subtract: 0 - 2 - 4 = " + str(result))
	def test_multiply(self):
		result = rpn.calculate("3 5 6 *")
		self.assertEqual(90, result)
		print("Passed multiply: 3 * 5 * 6 = " + str(result))
	def test_divide(self):
		result = rpn.calculate("4 8 /")
		self.assertEqual(2, result)
		print("Passed divide: 8 / 4 = " + str(result))
	def test_power(self):
		result = rpn.calculate("7 2 ^")
		self.assertEqual(128, result)
		print("Passed power: 2 ^ 7 = " + str(result))
