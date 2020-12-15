import unittest
from models.treatment import Treatment


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.test_treat_clipclaw = Treatment(
            1, 1, "15/06/2020", "Clipped claws", 5)
        self.test_treat_wormtabs = Treatment(
            1, 1, "01/02/2020", "Given worming tablets", 4)
        self.test_treat_checkup = Treatment(
            1, 1, "29/12/2019", "regular checkup", 3)
        self.test_treat_scan = Treatment(2, 1, "15/11/2019", "MRI scan", 10)
