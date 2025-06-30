import unittest
from src.compress_string import compress_string

class TestCompressString(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")

    def test_no_repeats(self):
        self.assertEqual(compress_string("abcdef"), "abcdef")

    def test_empty(self):
        self.assertEqual(compress_string(""), "")

    def test_single_char(self):
        self.assertEqual(compress_string("a"), "a")

    def test_mixed(self):
        self.assertEqual(compress_string("aaabbc"), "aaabbc")

    def test_compressed_not_shorter(self):
        self.assertEqual(compress_string("abc"), "abc")
        self.assertEqual(compress_string("aabb"), "aabb")

    def test_numbers(self):
        self.assertEqual(compress_string("111223"), "111223")

    def test_long(self):
        self.assertEqual(compress_string("aaaaaaaaaa"), "a10")

if __name__ == "__main__":
    unittest.main()

