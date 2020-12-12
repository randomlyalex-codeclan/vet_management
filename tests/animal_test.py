import unittest
from models.animal import Animal
from models.vet import Vet


class TestAnimal(unittest.TestCase):
    def setUp(self):
        test_vet_peter = Vet("Peter")
        test_vet_mark = Vet("Mark")
        test_vet_paul = Vet("Paul")

        self.test_animal_pepper = Animal(
            "Pepper", "10/11/2015", "Horse", "Roddy, Ireland", test_vet_paul)
        self.test_animal_luna = Animal(
            "Mika", "01/03/2012", "Cat", "Live, Edinburgh", test_vet_mark)
        self.test_animal_buddy = Animal(
            "Buddy", "19/01/2014", "Rabbit", "Maddie, Glasgow", test_vet_peter)
        self.test_animal_snowy = Animal(
            "Snowy", "17/02/2015", "Dog", "Jen, Liverpool", test_vet_peter)
        self.test_animal_lola = Animal(
            "Lola", "04/08/2018", "Cow", "Farmer Joe", test_vet_peter)
        self.test_animal_apollo = Animal(
            "Apollo", "22/03/2016", "Dog", "Carl, London", test_vet_paul)
        self.test_animal_buster = Animal(
            "Buster", "29/04/2019", "Dog", "Sam, Newcastle", test_vet_paul)
        self.test_animal_izzy = Animal(
            "Izzy", "30/05/2020", "Cat", "Ali, Manchester", test_vet_mark)

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
        self.assertEqual("Roddy, Ireland", self.test_animal_pepper.owner)
        self.assertEqual("Jen, Liverpool", self.test_animal_snowy.owner)
        self.assertEqual("Sam, Newcastle", self.test_animal_buster.owner)

    def test_animal_has_a__vet(self):
        self.assertEqual("Paul", self.test_animal_pepper.vet.name)
        self.assertEqual("Peter", self.test_animal_snowy.vet.name)
        self.assertEqual("Paul", self.test_animal_buster.vet.name)

    def test_add_treatment_to_animal(self):
        # test no treatment
        self.assertEqual("", self.test_animal_snowy.treatments)
        self.test_animal_snowy.add_treatment("Clip Claws")
        self.assertEqual("Clip Claws", self.test_animal_snowy.treatments)

    def test_add_two_treatments_to_animal_expect_comma(self):
        self.test_animal_snowy.add_treatment("Clip Claws")
        self.test_animal_snowy.add_treatment("Worms Tablets")
        self.assertEqual("Clip Claws, Worms Tablets",
                         self.test_animal_snowy.treatments)

    def test_add_three_treatments_to_animal_expect_commas(self):
        self.test_animal_snowy.add_treatment("Clip Claws")
        self.test_animal_snowy.add_treatment("Worms Tablets")
        self.test_animal_snowy.add_treatment("Regular Checkup")
        self.assertEqual("Clip Claws, Worms Tablets, Regular Checkup",
                         self.test_animal_snowy.treatments)

    def test_clear_treatments(self):
        self.test_animal_snowy.add_treatment("Clip Claws")
        self.test_animal_snowy.add_treatment("Worms Tablets")
        self.test_animal_snowy.add_treatment("Regular Checkup")
        self.test_animal_snowy.clear_treatment_history()
        self.assertEqual("", self.test_animal_snowy.treatments)

    def test_remove_last_treatment(self):
        self.test_animal_snowy.add_treatment("Clip Claws")
        self.test_animal_snowy.add_treatment("Worms Tablets")
        self.test_animal_snowy.add_treatment("Regular Checkup")
        self.test_animal_snowy.remove_last_treatment()
        self.assertEqual("Clip Claws, Worms Tablets",
                         self.test_animal_snowy.treatments)
