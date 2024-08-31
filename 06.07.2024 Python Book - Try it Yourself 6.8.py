def loop(dictn):
    cont = 1
    for key, value in dictn.items():
        if cont == 1:
            print("\n Here is what I know about {}".format(dictn["Name"]))
        else:
            print("His(Her) {} is {}".format(key, value))
        cont += 1
		
apollo = {"Name": "Apollo", "Kind": "Dog", "Owner": "Bufalo Prod. Limpeza"}
ellie = {"Name": "Ellie", "Kind": "Dog", "Owner": "William"}
princesa = {"Name": "Princesa", "Kind": "Dog", "Owner": "Grandmother"}
pets = [apollo, ellie, princesa]

for pet in pets:
    loop(pet)
