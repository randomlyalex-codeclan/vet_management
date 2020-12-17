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

test_vet_sam = Vet("Dr. Sam", False)
test_vet_alison = Vet("Dr. Alison", False)
test_vet_joe = Vet("Dr. Joe", False)


test_owner_david = Owner("David", "Edinburgh", False)
test_owner_peter = Owner("Peter Griffin", "Quahog", False)
test_owner_jamie = Owner("Jamie", "Glasgow", False)
test_owner_sarah = Owner("Sarah", "London", False)


test_animal_big_bird = Animal(
    "Big Bird", "10/11/2015", "Bird", test_owner_david, test_vet_sam, False)
test_animal_earnie = Animal(
    "Earnie ", "01/03/2012", "Giant Chicken", test_owner_david, test_vet_sam, False)
test_animal_brian = Animal(
    "Brian", "19/01/2014", "Dog", test_owner_peter, test_vet_joe, False)
test_animal_evil_monkey = Animal(
    "Evil Monkey", "17/02/2015", "Monkey", test_owner_jamie, test_vet_joe, False)
test_animal_vinny = Animal(
    "Vinny", "04/08/2018", "Dog", test_owner_jamie, test_vet_joe, False)
test_animal_apollo = Animal(
    "Apollo", "22/03/2016", "Dog", test_owner_jamie, test_vet_sam, False)
test_animal_buster = Animal(
    "Buster", "29/04/2019", "Dog", test_owner_sarah, test_vet_sam, False)
test_animal_izzy = Animal(
    "Izzy", "30/05/2020", "Cat", test_owner_sarah, test_vet_alison, False)

test_treat_clipclaw = Treatment(1, 1, "15/06/2020", "Clipped claws", 5)
test_treat_wormtabs = Treatment(2, 3, "01/02/2020", "Given worming tablets", 4)
test_treat_checkup = Treatment(3, 3, "29/12/2019", "Regular checkup", 3)
test_treat_4 = Treatment(4, 2, "15/11/2019", "Broken arm", 5)
test_treat_5 = Treatment(4, 2, "15/11/2019", "Dental surgeries", 3)
test_treat_6 = Treatment(4, 2, "15/11/2019", "Tooth Extraction", 8)
test_treat_7 = Treatment(4, 1, "15/11/2019", "Neutering", 9)
test_treat_8 = Treatment(4, 2, "15/11/2019", "Skin Surgeries", 6)
# --------

# save three 3 vets
vet_repository.save(test_vet_sam)
vet_repository.save(test_vet_joe)
vet_repository.save(test_vet_alison)
# save 4 owners
owner_repository.save(test_owner_david)
owner_repository.save(test_owner_peter)
owner_repository.save(test_owner_jamie)
owner_repository.save(test_owner_sarah)

# save 7 animals
animal_repository.save(test_animal_big_bird)
animal_repository.save(test_animal_earnie)
animal_repository.save(test_animal_brian)
animal_repository.save(test_animal_evil_monkey)
animal_repository.save(test_animal_buster)
animal_repository.save(test_animal_izzy)
animal_repository.save(test_animal_vinny)
animal_repository.save(test_animal_apollo)

# create some treatments
treatment_repository.save(test_treat_clipclaw)
treatment_repository.save(test_treat_wormtabs)
treatment_repository.save(test_treat_checkup)
treatment_repository.save(test_treat_4)
treatment_repository.save(test_treat_5)
treatment_repository.save(test_treat_6)
treatment_repository.save(test_treat_7)
treatment_repository.save(test_treat_8)

# select all vets and print
vets = vet_repository.select_all()
for vet in vets:
    print(vet.__dict__)

# select all owners and print
owners = owner_repository.select_all()
for owner in owners:
    print(owner.__dict__)

# select all animals and print
animals = animal_repository.select_all()
for animal in animals:
    print(animal.__dict__)

# select all animals and print
treatments = treatment_repository.select_all()
for treatment in treatments:
    print(treatment.__dict__)

# # # test delete_all animals
# # animal_repository.delete_all()
# # # test delete_all vets
# # vet_repository.delete_all()

# # test delete by id some values
# animal_repository.delete_id(4)
# animal_repository.delete_id(5)

# vet_repository.delete_id(3)
# vet_repository.delete_id(2)


# print("\n", "\n")
# # select all vets and print
# vets = vet_repository.select_all()
# for vet in vets:
#     print(vet.__dict__)
# # select all animals and print
# animals = animal_repository.select_all()
# for animal in animals:
#     print(animal.__dict__)

# # testing selecting changing and updating animals:
# snowy = animal_repository.select_id(3)


# # testing selecting changing and updating vets:
# vet = vet_repository.select_id(1)
# vet.name = "Trevor"
# vet_repository.update(vet)


# print("\n", "\n")
# # select all vets and print
# vets = vet_repository.select_all()
# for vet in vets:
#     print(vet.__dict__)
# # select all animals and print
# animals = animal_repository.select_all()
# for animal in animals:
#     print(animal.__dict__)
