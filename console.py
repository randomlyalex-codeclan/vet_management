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
