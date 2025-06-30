import unittest
from src.reverse_words import reverse_words

class TestReverseWords(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(reverse_words("hello world"), "world hello")

    def test_multiple_spaces(self):
        self.assertEqual(reverse_words("a  b   c"), "c b a")

    def test_leading_trailing_spaces(self):
        self.assertEqual(reverse_words("  hello world  "), "world hello")

    def test_single_word(self):
        self.assertEqual(reverse_words("hello"), "hello")

    def test_empty(self):
        self.assertEqual(reverse_words(""), "")

    def test_punctuation(self):
        self.assertEqual(reverse_words("hello, world!"), "world! hello,")

if __name__ == "__main__":
    unittest.main()
