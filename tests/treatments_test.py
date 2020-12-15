import unittest
from models.treatment import Treatment


class TestOwner(unittest.TestCase):
    def setUp(self):
        test_treat_clipclaw = Owner("David", "Edinburgh")
        test_treat_wormtabs = Owner("Carl", "liverpool")
        test_treat_checkup = Owner("Carl", "liverpool")
        


