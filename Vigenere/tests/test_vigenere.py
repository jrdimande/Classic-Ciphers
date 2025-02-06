import unittest
from Vigenere.modules.vigenere import CipherVigenere


class TestVigener(unittest.TestCase):
    def test_encrypt(self):
        cipher = CipherVigenere()
        result = cipher.encrypt("oi", "key")
        self.assertEqual(result, "YM")

    def test_decrypy(self):
        cipher = CipherVigenere()
        result = cipher.decrypt("YM", "key")
        self.assertEqual(result, "OI")



if __name__ == "__main__":
    unittest.main()

