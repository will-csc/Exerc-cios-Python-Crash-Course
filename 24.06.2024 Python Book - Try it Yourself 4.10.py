list_languages = ["English","Portuguese","Espanõl","Russian","Italian",
				  "Arabian","French"]

#----------- 1 ---------------
print("The first three languages are:")
for lang in list_languages[:3]:
	print(lang)

#---------- 2 --------------
print("\nThree items from the middle of the list are:")
middle_of_list = len(list_languages) // 2 - 1
for lang in list_languages[middle_of_list:middle_of_list+3]:
	print(lang)

#---------- 2 --------------
print("\nThe last three items from the list are:")
for lang in list_languages[len(list_languages)-3:]:
	print(lang)
