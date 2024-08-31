def make_sandwich(*items):
    print("Making a sandwich with the following items:")
    for item in items:
        print(f"- {item}")
    print("Sandwich is ready!\n")

# Example calls to make_sandwich function
make_sandwich('Ham', 'Cheese')
make_sandwich('Turkey', 'Lettuce', 'Tomato')
make_sandwich('Peanut Butter', 'Jelly', 'Banana', 'Honey')
