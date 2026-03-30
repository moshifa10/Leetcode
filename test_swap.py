import unittest
from swap import swap
# from your_file import swap

class TestStringSwap(unittest.TestCase):

    # ✅ Example case
    def test_valid_swap(self):
        self.assertTrue(swap("bank", "kanb"))

    # ✅ Already equal (no swap needed)
    def test_already_equal(self):
        self.assertTrue(swap("abc", "abc"))

    # ❌ More than one swap needed
    def test_more_than_one_swap_needed(self):
        self.assertFalse(swap("abcd", "badc"))

    # ❌ Different characters
    def test_different_characters(self):
        self.assertFalse(swap("abc", "def"))

    # ❌ Same length but impossible swap
    def test_impossible_case(self):
        self.assertFalse(swap("ab", "ca"))

    # ✅ Exactly one swap possible
    def test_two_characters(self):
        self.assertTrue(swap("ab", "ba"))

    # ❌ Only one character different
    def test_one_difference(self):
        self.assertFalse(swap("ab", "ac"))

    # ✅ Repeated characters (important edge case)
    def test_repeated_characters_valid(self):
        self.assertTrue(swap("aa", "aa"))

    # ❌ Repeated characters but invalid
    def test_repeated_characters_invalid(self):
        self.assertFalse(swap("abca", "abcb"))

    # ❌ Different lengths (should fail safely)
    def test_different_lengths(self):
        self.assertFalse(swap("abc", "ab"))


if __name__ == "__main__":
    unittest.main()