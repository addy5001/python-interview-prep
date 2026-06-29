import unittest
from string_operations import StringOperations


class TestStringOperations(unittest.TestCase):
    def setUp(self):
        self.ops = StringOperations()

    def test_empty_strings(self):
        self.assertTrue(self.ops.isAnagram("", ""))

    def test_different_lengths(self):
        self.assertFalse(self.ops.isAnagram("abc", "ab"))

    def test_valid_anagram(self):
        self.assertTrue(self.ops.isAnagram("anagram", "nagaram"))

    def test_invalid_anagram(self):
        self.assertFalse(self.ops.isAnagram("rat", "car"))

    def test_same_characters_different_counts(self):
        self.assertFalse(self.ops.isAnagram("aab", "abb"))

    def test_case_sensitivity(self):
        # Unless specified, anagrams are case-sensitive.
        # "Anagram" has 'A' and 'a', "nagaram" has only lowercase 'a'.
        self.assertFalse(self.ops.isAnagram("Anagram", "nagaram"))

    def test_with_spaces(self):
        self.assertTrue(self.ops.isAnagram("a dec", "ced a"))
        self.assertFalse(self.ops.isAnagram("a dec", "ceda"))

    def test_concatenation_empty(self):
        self.assertEqual(self.ops.getConcatenation([]), [])

    def test_concatenation_single_element(self):
        self.assertEqual(self.ops.getConcatenation([1]), [1, 1])

    def test_concatenation_multiple_elements(self):
        self.assertEqual(self.ops.getConcatenation([1, 2, 3]), [1, 2, 3, 1, 2, 3])

    def test_lcp_empty_list(self):
        self.assertEqual(self.ops.longestCommonPrefix([]), "")

    def test_lcp_single_string(self):
        self.assertEqual(self.ops.longestCommonPrefix(["apple"]), "apple")

    def test_lcp_common_prefix_exists(self):
        self.assertEqual(self.ops.longestCommonPrefix(["flower", "flow", "flight"]), "fl")

    def test_lcp_no_common_prefix(self):
        self.assertEqual(self.ops.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_lcp_exact_matches(self):
        self.assertEqual(self.ops.longestCommonPrefix(["apple", "apple", "apple"]), "apple")


