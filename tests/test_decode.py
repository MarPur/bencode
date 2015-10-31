import unittest

from bencode import decode


class DecodeBencodeTest(unittest.TestCase):

    def test_decode_int(self):
        self.assertEqual(decode(b'i1e'), 1)
        self.assertEqual(decode(b'i1000e'), 1000)
        self.assertEqual(decode(b'i-1000e'), -1000)
        self.assertEqual(decode(b'i0e'), 0)

    def test_decode_string(self):
        self.assertEqual(decode(b'4:abcd'), 'abcd')
        self.assertEqual(decode(b'1:a'), 'a')
        self.assertEqual(decode(b'0:'), '')

    def test_decode_list(self):
        self.assertEqual(decode(b'le'), [])
        self.assertEqual(decode(b'li1ei100e2:eee'), [1, 100, 'ee'])
        self.assertEqual(decode(b'lllleeee'), [[[[]]]])
        self.assertEqual(decode(b'lllleee4:abcdi10ee'), [[[[]]], 'abcd', 10])

    def test_decode_dictionary(self):
        self.assertEqual(decode(b'de'), {})
        self.assertEqual(decode(b'd1:1i1ee'), {'1': 1})
        self.assertEqual(decode(b'd1:1i1e4:abcd3:abce'), {'1': 1, 'abcd': 'abc'})
        self.assertEqual(decode(b'd0:i1e4:abcd3:abce'), {'': 1, 'abcd': 'abc'})
        self.assertEqual(decode(b'd1:ali10e3:abcded1:a1:beee'), {'a': [10, 'abc', {}, {'a': 'b'}]})


if __name__ == '__main__':
    unittest.main()