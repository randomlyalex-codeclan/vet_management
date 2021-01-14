import unittest
from models.animal import Animal
from models.vet import Vet
from models.owner import Owner


class TestAnimal(unittest.TestCase):
    def setUp(self):
        test_vet_peter = Vet("Peter", False)
        test_vet_mark = Vet("Mark", False)
        test_vet_paul = Vet("Paul", False)

        test_owner_david = Owner("David", "Edinburgh", False)
        test_owner_carl = Owner("Carl", "liverpool", False)
        test_owner_jamie = Owner("Jamie", "Glasgow", False)
        test_owner_sarah = Owner("Sarah", "London", False)

        self.test_animal_pepper = Animal(
            "Pepper", "10/11/2015", "Horse", test_owner_david, test_vet_paul, False)
        self.test_animal_luna = Animal(
            "Mika", "01/03/2012", "Cat", test_owner_david, test_vet_mark, False)
        self.test_animal_buddy = Animal(
            "Buddy", "19/01/2014", "Rabbit", test_owner_carl, test_vet_peter, False)
        self.test_animal_snowy = Animal(
            "Snowy", "17/02/2015", "Dog", test_owner_carl, test_vet_peter, False)
        self.test_animal_lola = Animal(
            "Lola", "04/08/2018", "Cow", test_owner_jamie, test_vet_peter, False)
        self.test_animal_apollo = Animal(
            "Apollo", "22/03/2016", "Dog", test_owner_jamie, test_vet_paul, False)
        self.test_animal_buster = Animal(
            "Buster", "29/04/2019", "Dog", test_owner_sarah, test_vet_paul, False)
        self.test_animal_izzy = Animal(
            "Izzy", "30/05/2020", "Cat", test_owner_sarah, test_vet_mark, False)

    def test_animal_has_a__name(self):
        self.assertEqual("Pepper", self.test_animal_pepper.name)
        self.assertEqual("Snowy", self.test_animal_snowy.name)
        self.assertEqual("Buster", self.test_animal_buster.name)

    def test_animal_has_a__dob(self):
        self.assertEqual("10/11/2015", self.test_animal_pepper.dob)
        self.assertEqual("17/02/2015", self.test_animal_snowy.dob)
        self.assertEqual("29/04/2019", self.test_animal_buster.dob)

    def test_animal_has_a__species(self):
        self.assertEqual("Horse", self.test_animal_pepper.species)
        self.assertEqual("Dog", self.test_animal_snowy.species)
        self.assertEqual("Dog", self.test_animal_buster.species)

    def test_animal_has_a__owner(self):
        self.assertEqual("David", self.test_animal_pepper.owner.name)
        self.assertEqual("Carl", self.test_animal_snowy.owner.name)
        self.assertEqual("Sarah", self.test_animal_buster.owner.name)

    def test_animal_has_a__vet(self):
        self.assertEqual("Paul", self.test_animal_pepper.vet.name)
        self.assertEqual("Peter", self.test_animal_snowy.vet.name)
        self.assertEqual("Paul", self.test_animal_buster.vet.name)
