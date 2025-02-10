import unittest
from Vigenere.modules.vigenere import check_key

class TestCheck(unittest.TestCase):
    def test_check_key(self):
        entry = (check_key('hello'))
        self.assertEqual(entry, False)



if __name__ == '__main__':
    unittest.main()