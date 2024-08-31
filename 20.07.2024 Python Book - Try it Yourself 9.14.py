from random import randint

class Die():
	
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		print(f"The die has exactly {self.sides}")
		print(f"The number the die gave is: {randint(1,self.sides)}")
		
die = Die(8)
for i in range(10):
	die.roll_die()
