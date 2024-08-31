from city_functions import city_country
import unittest

class NamesTestCase(unittest.TestCase):
	
	"""Tests for 'name_function.py'."""
	def test_city_country(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = city_country('Santiago', 'Chile'," 19.6 million")
		self.assertEqual(formatted_name, 'Santiago,Chile - population 19.6 million')
		
unittest.main()
