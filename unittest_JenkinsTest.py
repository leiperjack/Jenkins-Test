import unittest
#hi
from JenkinsTest import add

class myClass(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,4), (7))


if __name__ == "__main__":
    unittest.main()
