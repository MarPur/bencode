import unittest

from bencode import encode


class EncodeBencodeTest(unittest.TestCase):

    def test_encodes_string(self):
        self.assertEqual(encode('string'), b'6:string')
        self.assertEqual(encode('string_string'), b'13:string_string')
        self.assertEqual(encode(''), b'0:')
        self.assertEqual(encode(b'123456'), b'6:123456')
        self.assertEqual(encode(b'\xbc\x94\x1f\x05'), b'4:\xbc\x94\x1f\x05')

    def test_does_not_encode_invalid_values(self):
        self.assertRaises(ValueError, encode, set())
        self.assertRaises(ValueError, encode, (0, 1))
        self.assertRaises(ValueError, encode, 1.0)

    def test_encode_integer(self):
        self.assertEqual(encode(1), b'i1e')
        self.assertEqual(encode(1000), b'i1000e')
        self.assertEqual(encode(0), b'i0e')
        self.assertEqual(encode(-100), b'i-100e')

    def test_encode_list(self):
        self.assertEqual(encode([]), b'le')
        self.assertEqual(encode([1, 2, 3, -5]), b'li1ei2ei3ei-5ee')
        self.assertEqual(encode(['a', 'aaa', 0, '']), b'l1:a3:aaai0e0:e')
        self.assertEqual(encode(['a', [1, 2, 3], [0, '']]), b'l1:ali1ei2ei3eeli0e0:ee')
        self.assertEqual(encode([[[]]]), b'llleee')

    def test_encode_dictionary(self):
        self.assertEqual(encode({}), b'de')
        self.assertEqual(encode({'a': 1, 'b': 3, 'c': [1, 2, 3]}), b'd1:ai1e1:bi3e1:cli1ei2ei3eee')
        self.assertEqual(encode({'a': {'b': {'c': {'d': 0}}}}), b'd1:ad1:bd1:cd1:di0eeeee')


if __name__ == '__main__':
    unittest.main()