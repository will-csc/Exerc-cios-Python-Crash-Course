import unittest

class Employee():
	
	def __init__(self,first_name,last_name,annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary
	
	def give_raise(self,increase=5000):
		self.annual_salary += increase
		
class TestEmployee(unittest.TestCase):
	
    def setUp(self):
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
