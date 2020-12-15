# this will be used to quick and dirty end to end test CRUD but prior to passing to jinja templates and flask.

from models.vet import Vet
from models.animal import Animal
from models.treatment import Treatment
from models.owner import Owner

import repositories.animal_repository as animal_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.treatment_repository as treatment_repository

# consol_setUp so I can use later ----

test_vet_peter = Vet("Peter", False)
test_vet_mark = Vet("Mark", False)
test_vet_paul = Vet("Paul", False)

test_owner_david = Owner("David", "Edinburgh", False)
test_owner_carl = Owner("Carl", "liverpool", False)
test_owner_jamie = Owner("Jamie", "Glasgow", False)
test_owner_sarah = Owner("Sarah", "London", False)


test_animal_pepper = Animal(
    "Pepper", "10/11/2015", "Horse", test_owner_david, test_vet_paul, False)
test_animal_luna = Animal(
    "Luna", "01/03/2012", "Cat", test_owner_david, test_vet_mark, False)
test_animal_buddy = Animal(
    "Buddy", "19/01/2014", "Rabbit", test_owner_carl, test_vet_peter, False)
test_animal_snowy = Animal(
    "Snowy", "17/02/2015", "Dog", test_owner_carl, test_vet_peter, False)
test_animal_lola = Animal(
    "Lola", "04/08/2018", "Cow", test_owner_jamie, test_vet_peter, False)
test_animal_apollo = Animal(
    "Apollo", "22/03/2016", "Dog", test_owner_jamie, test_vet_paul, False)
test_animal_buster = Animal(
    "Buster", "29/04/2019", "Dog", test_owner_sarah, test_vet_paul, False)
test_animal_izzy = Animal(
    "Izzy", "30/05/2020", "Cat", test_owner_sarah, test_vet_mark, False)


# --------

# save three 3 vets
vet_repository.save(test_vet_peter)
vet_repository.save(test_vet_mark)
vet_repository.save(test_vet_paul)
# save 4 owners
owner_repository.save(test_owner_david)
owner_repository.save(test_owner_carl)
owner_repository.save(test_owner_jamie)
owner_repository.save(test_owner_sarah)

# save 7 animals
animal_repository.save(test_animal_pepper)
animal_repository.save(test_animal_luna)
animal_repository.save(test_animal_snowy)
animal_repository.save(test_animal_lola)
animal_repository.save(test_animal_buster)
animal_repository.save(test_animal_izzy)
animal_repository.save(test_animal_mikka)
animal_repository.save(test_animal_buddy)


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
