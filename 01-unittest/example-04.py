import unittest
import tempfile
import time
import sys


class TestOnTemporaryFile(unittest.TestCase):
    def setUp(self):
        print(f"Running {self.__class__} setup")
        self.tmp_file = tempfile.TemporaryFile(mode="w+t")

    def tearDown(self):
        print(f"Running {self.__class__} teardown")
        self.tmp_file.close()

    def test_file_write(self):
        print("Running test_file_write test")
        bytes_written = self.tmp_file.write("Hello!")
        self.assertEqual(bytes_written, 6)


class TestPlatformSpecific(unittest.TestCase):
    @unittest.skip("This test is not ready")
    def test_not_ready(self):
        self.fail("I should have been skipped!")

    @unittest.skipUnless(sys.platform == "linux", "requires linux")
    def test_get_boottime_clock(self):
        self.assertIn("CLOCK_BOOTTIME", dir(time))

    @unittest.skipIf(sys.version_info.major < 3, "For Python 3.X only")
    def test_string_instance(self):
        self.assertEqual(5 / 2, 2.5)  # this fails for Python 2.X
        self.assertEqual(5 // 2, 2)
