import unittest


class TestBuiltins(unittest.TestCase):
    def test_membership(self):
        self.assertIn("A", "Andalusia")
        self.assertTrue("A" in "Andalusia")

    def test_instances(self):
        self.assertIsInstance('a', int)
        self.assertTrue(isinstance(5, int))

    def test_falsehood(self):
        self.assertFalse(True)


if __name__ == "__main__":
    unittest.main()
