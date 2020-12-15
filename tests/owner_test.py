import unittest
from models.owner import Owner


class TestOwner(unittest.TestCase):
    def setUp(self):
        test_owner_david = Owner("David", "Edinburgh")
        test_owner_carl = Owner("Carl", "liverpool")
        test_owner_jamie = Owner("Jamie", "Glasgow")

