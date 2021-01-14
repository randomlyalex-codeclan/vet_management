import unittest
from models.vet import Vet


class TestVet(unittest.TestCase):
    def setUp(self):
        self.test_vet_peter = Vet("Peter", False)
        self.test_vet_mark = Vet("Mark", False)
        self.test_vet_paul = Vet("Paul", False)

    def test_vet_has_a__name(self):
        self.assertEqual("Peter", self.test_vet_peter.name)
        self.assertEqual("Mark", self.test_vet_mark.name)
        self.assertEqual("Paul", self.test_vet_paul.name)
