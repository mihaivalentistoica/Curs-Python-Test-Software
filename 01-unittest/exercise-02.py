import unittest


class TestIntegers(unittest.TestCase):
    def test_atoi(self):
        self.assertEqual(int("10973"), 10973)

    def test_itoa(self):
        self.assertEqual(str(10_974_553), "10974553")

    def test_bin_to_dec(self):
        self.assertEqual(int("010101", 2), 21)

    def test_dec_to_hex(self):
        self.assertEqual(hex(777), "0x309")


class TestStrings(unittest.TestCase):
    def test_slicing(self):
        self.assertEqual("pineapple"[3:7], "eapp")

    def test_formatting(self):
        tuple_ = (1,)
        self.assertEqual(f"{tuple_}", "(1,)")

    def test_membership(self):
        self.assertIn("x", "xyz")
