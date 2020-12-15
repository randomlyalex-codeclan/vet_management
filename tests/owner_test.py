import unittest
from models.owner import Owner


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.test_owner_david = Owner("David", "Edinburgh", False)
        self.test_owner_carl = Owner("Carl", "liverpool", False)
        self.test_owner_jamie = Owner("Jamie", "Glasgow", False)
        self.test_owner_sarah = Owner("Sarah", "London", False)
