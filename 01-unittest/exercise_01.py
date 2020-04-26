import unittest


class TestBuiltins(unittest.TestCase):
    def test_membership_fails(self):
        self.assertIn("A", "Sao Paulo")

    def test_instances_fails(self):
        self.assertIsInstance(5, list)

    def test_falsehood_fails(self):
        self.assertTrue(False)


if __name__ == "__main__":
    unittest.main()
