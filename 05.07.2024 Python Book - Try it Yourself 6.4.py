def looping(dictionary):
	for key,value in sorted(dictionary.items()):
		print("\n The meaning of {} is: \n{}".format(key,value))

if __name__ = '__main__':
	python_keywords = {"Key":"Stores a value",
				   "Value":"Any value",
				   "If":"Conditional key word",
				   "Tuple":"An unchangeble list",
				   "Set":"An grouped data without repetition",
				   "List":"List of values"}
	looping(python_keywords)
	print("\n Adding more keys and values to the dictionary \n")
	python_keywords["Loop"] = "Iteration through all values"
	python_keywords["Print"] = "Print something to the user"
	python_keywords["dictionary"] = "Store values based on keys"
	python_keywords["Class"] = "An object with attributes and characteristics"
	python_keywords["Append"] = "Add more values to a list"
	looping(python_keywords)
