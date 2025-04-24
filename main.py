# main.py

from pet import Pet

# Creating the pet
pet_name = input("Enter your pet's name: ")
my_pet = Pet(pet_name)
print(f"Creating pet: {my_pet.name}")

# Simulate actions
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Train tricks
my_pet.train("spin")
my_pet.train("shake paws")

# Show status
my_pet.get_status()

