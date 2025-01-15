import unittest
from cesar import CipherCesar


class TestCipherCesar(unittest.TestCase):
    def test_encrypt(self):
        cipher = CipherCesar()
        result = cipher.encrypt("abc")
        self.assertEqual(result, "BCD")

    def test_decrypt(self):
        cipher = CipherCesar()
        result = cipher.decrypt(("BCD"))
        self.assertEqual(result, "ABC")




if __name__ == "__main__":
    unittest.main()