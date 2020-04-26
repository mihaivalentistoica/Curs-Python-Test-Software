import unittest
from library import Library


class TestLibraryInventory(unittest.TestCase):
    def test_library_init(self):
        library = Library()
        self.assertDictEqual(library.books_by_title, {})
