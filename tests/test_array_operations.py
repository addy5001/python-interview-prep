import unittest
from array_operations import ArrayOperations


class TestArrayOperations(unittest.TestCase):
    def setUp(self):
        self.ops = ArrayOperations()

    def test_empty_array(self):
        self.assertFalse(self.ops.contains_duplicates([]))

    def test_single_element(self):
        self.assertFalse(self.ops.contains_duplicates([1]))

    def test_no_duplicates(self):
        self.assertFalse(self.ops.contains_duplicates([1, 2, 3, 4, 5]))

    def test_with_duplicates(self):
        self.assertTrue(self.ops.contains_duplicates([1, 2, 3, 1]))

    def test_all_same_elements(self):
        self.assertTrue(self.ops.contains_duplicates([7, 7, 7, 7]))

    def test_negative_numbers_no_duplicates(self):
        self.assertFalse(self.ops.contains_duplicates([-1, -2, -3, 0]))

    def test_negative_numbers_with_duplicates(self):
        self.assertTrue(self.ops.contains_duplicates([-1, -2, -1, 0]))

    def test_duplicate_at_beginning(self):
        self.assertTrue(self.ops.contains_duplicates([5, 5, 1, 2, 3, 4]))

    def test_duplicate_at_end(self):
        self.assertTrue(self.ops.contains_duplicates([1, 2, 3, 4, 5, 5]))

    def test_sorted_empty_array(self):
        self.assertFalse(self.ops.contains_duplicates_with_sorting([]))

    def test_sorted_single_element(self):
        self.assertFalse(self.ops.contains_duplicates_with_sorting([1]))

    def test_sorted_no_duplicates(self):
        self.assertFalse(self.ops.contains_duplicates_with_sorting([1, 2, 3, 4, 5]))

    def test_sorted_with_duplicates(self):
        self.assertTrue(self.ops.contains_duplicates_with_sorting([1, 2, 2, 3, 4]))

    def test_sorted_duplicate_at_beginning(self):
        self.assertTrue(self.ops.contains_duplicates_with_sorting([1, 1, 2, 3, 4]))

    def test_sorted_duplicate_at_end(self):
        self.assertTrue(self.ops.contains_duplicates_with_sorting([1, 2, 3, 4, 4]))

    def test_sorted_negative_numbers(self):
        self.assertTrue(self.ops.contains_duplicates_with_sorting([-5, -5, -3, 0, 1]))

    def test_sorted_unsorted_no_duplicates(self):
        self.assertFalse(self.ops.contains_duplicates_with_sorting([3, 1, 5, 4, 2]))

    def test_sorted_unsorted_with_duplicates(self):
        self.assertTrue(self.ops.contains_duplicates_with_sorting([3, 1, 5, 1, 2]))

    def test_two_sum_exists(self):
        self.assertEqual(self.ops.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_duplicates(self):
        self.assertEqual(self.ops.twoSum([3, 3], 6), [0, 1])

    def test_two_sum_unsorted(self):
        self.assertEqual(self.ops.twoSum([3, 2, 4], 6), [1, 2])

    def test_two_sum_no_solution(self):
        self.assertEqual(self.ops.twoSum([1, 2, 3], 7), [])

    def test_remove_element_empty(self):
        nums = []
        k = self.ops.removeElement(nums, 3)
        self.assertEqual(k, 0)
        self.assertEqual(nums, [])

    def test_remove_element_no_matches(self):
        nums = [1, 2, 3, 4]
        k = self.ops.removeElement(nums, 5)
        self.assertEqual(k, 4)
        self.assertEqual(sorted(nums[:k]), [1, 2, 3, 4])

    def test_remove_element_all_matches(self):
        nums = [3, 3, 3]
        k = self.ops.removeElement(nums, 3)
        self.assertEqual(k, 0)

    def test_remove_element_mixed(self):
        nums = [3, 2, 2, 3]
        k = self.ops.removeElement(nums, 3)
        self.assertEqual(k, 2)
        self.assertEqual(sorted(nums[:k]), [2, 2])





