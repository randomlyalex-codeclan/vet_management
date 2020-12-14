# this will be used to quick and dirty end to end test CRUD but prior to passing to jinja templates and flask.

from models.vet import Vet
from models.animal import Animal

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository

# consol_setUp so I can use later ----

test_vet_peter = Vet("Peter")
test_vet_mark = Vet("Mark")
test_vet_paul = Vet("Paul")

test_animal_pepper = Animal(
    "Pepper", "10/11/2015", "Horse", "Roddy, Ireland", test_vet_paul)
test_animal_luna = Animal(
    "Mika", "01/03/2012", "Cat", "Live, Edinburgh", test_vet_mark)
test_animal_buddy = Animal(
    "Buddy", "19/01/2014", "Rabbit", "Maddie, Glasgow", test_vet_peter)
test_animal_snowy = Animal(
    "Snowy", "17/02/2015", "Dog", "Jen, Liverpool", test_vet_peter)
test_animal_lola = Animal(
    "Lola", "04/08/2018", "Cow", "Farmer Joe", test_vet_peter)
test_animal_apollo = Animal(
    "Apollo", "22/03/2016", "Dog", "Carl, London", test_vet_paul)
test_animal_buster = Animal(
    "Buster", "29/04/2019", "Dog", "Sam, Newcastle", test_vet_paul)
test_animal_izzy = Animal(
    "Izzy", "30/05/2020", "Cat", "Ali, Manchester", test_vet_mark)


# --------

# save three 3 vets
vet_repository.save(test_vet_peter)
vet_repository.save(test_vet_mark)
vet_repository.save(test_vet_paul)
# save 6 animals
animal_repository.save(test_animal_pepper)
animal_repository.save(test_animal_luna)
animal_repository.save(test_animal_snowy)
animal_repository.save(test_animal_lola)
animal_repository.save(test_animal_buster)
animal_repository.save(test_animal_izzy)

# select all vets and print
vets = vet_repository.select_all()
for vet in vets:
    print(vet.__dict__)
# select all animals and print
animals = animal_repository.select_all()
for animal in animals:
    print(animal.__dict__)

# # test delete_all animals
# animal_repository.delete_all()
# # test delete_all vets
# vet_repository.delete_all()

# test delete by id some values
animal_repository.delete_id(4)
animal_repository.delete_id(5)

vet_repository.delete_id(3)
vet_repository.delete_id(2)


print("\n", "\n")
# select all vets and print
vets = vet_repository.select_all()
for vet in vets:
    print(vet.__dict__)
# select all animals and print
animals = animal_repository.select_all()
for animal in animals:
    print(animal.__dict__)

# testing selecting changing and updating animals:
snowy = animal_repository.select_id(3)
snowy.add_treatment("Clip Claws")
snowy.add_treatment("Worms Tablets")
snowy.add_treatment("Regular Checkup")
animal_repository.update(snowy)

# testing selecting changing and updating vets:
vet = vet_repository.select_id(1)
vet.name = "Trevor"
vet_repository.update(vet)


print("\n", "\n")
# select all vets and print
vets = vet_repository.select_all()
for vet in vets:
    print(vet.__dict__)
# select all animals and print
animals = animal_repository.select_all()
for animal in animals:
    print(animal.__dict__)
