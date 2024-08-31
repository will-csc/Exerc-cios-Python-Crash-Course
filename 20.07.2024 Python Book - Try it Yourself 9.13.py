from collections import OrderedDict

python_keywords = OrderedDict()

dictionary = {"Key":"Stores a value",
				   "Value":"Any value",
				   "If":"Conditional key word",
				   "Tuple":"An unchangeble list",
				   "Set":"An grouped data without repetition",
				   "List":"List of values"}

for key,value in dictionary.items():
	python_keywords[key] = value
	
print(python_keywords)
	

				   
