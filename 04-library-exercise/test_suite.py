import unittest
# from test_book import TestBookInit, TestBookIsAvailable
# from test_library import TestLibraryInventory
import test_book
import test_library

test_suite = unittest.TestSuite(
    [test_book.TestBookInit('test_init'), test_book.TestBookInit('test_init_default_params'),
     test_book.TestBookIsAvailable('test_is_available'), test_library.TestLibraryInventory('test_library_init')])

# for test in test_suite:
#     test.run()
if __name__ == '__main__':
    # unittest.main()
    unittest.TextTestRunner().run(test_suite)
