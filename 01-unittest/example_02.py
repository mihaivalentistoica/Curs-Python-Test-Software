import unittest


class TestBuiltins(unittest.TestCase):
    def test_membership(self):
        self.assertIn("A", "Andalusia")
        self.assertTrue("A" in "Andalusia")

    def test_instances(self):
        self.assertIsInstance(5, int)
        self.assertTrue(isinstance(5, int))

    def test_falsehood(self):
        self.assertFalse(False)


# Notice missing unittest.main() call here.
