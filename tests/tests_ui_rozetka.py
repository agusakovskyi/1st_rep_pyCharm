import unittest
from utils.rozetka_utils import RozetkaUtils
class TestsRozetka(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rozetka_utils = RozetkaUtils()
        cls.rozetka_utils.open_rozetka_page()

    def test_search_random_item(self):
        self.rozetka_utils.search_random_item('asdfghjklo;p')

    def test_field_clear_button(self):
        self.rozetka_utils.validate_field_clear_button('some text')

    def test_search_item_via_main_search(self):
        self.rozetka_utils.search_item('Принтер')
        self.rozetka_utils.select_item_from_grid('Принтер')
        self.rozetka_utils.validate_selected_product_in_cart()

    def test_search_camelcase_item_via_main_search(self):
        self.rozetka_utils.search_item('пРиНтЕр')
        self.rozetka_utils.select_item_from_grid('пРиНтЕр')
        self.rozetka_utils.validate_selected_product_in_cart()





