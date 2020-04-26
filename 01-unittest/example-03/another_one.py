import unittest


class AnotherOne(unittest.TestCase):
    def test_thats_more_difficult_to_discover(self):
        self.assertDictEqual({}, {})
