import os
import unittest

if __name__ == "__main__":
    test_path = os.getcwd()
    suite = unittest.loader.TestLoader().discover(test_path)
    unittest.TextTestRunner(verbosity=2).run(suite)
