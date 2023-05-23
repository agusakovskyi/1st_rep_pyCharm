import unittest
from utils.rozetka_utils import RozetkaUtils
class TestsRozetka(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rozetka_utils = RozetkaUtils()
        cls.rozetka_utils.open_rozetka_page()

    def test_search_item_via_main_search(self):
        self.rozetka_utils.search_item('Принтер')