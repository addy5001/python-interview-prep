import unittest

from list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)

    def test_insert_head(self):
        ll = LinkedList()
        ll.insert(0, 10)
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll[0], 10)

    def test_insert_multiple(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll.insert(1, 20)
        ll.insert(2, 30)
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll[0], 10)
        self.assertEqual(ll[1], 20)
        self.assertEqual(ll[2], 30)

    def test_insert_at_beginning(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll.insert(0, 20)
        self.assertEqual(list(ll), [20, 10])

    def test_insert_in_middle(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll.insert(1, 30)
        ll.insert(1, 20)
        self.assertEqual(list(ll), [10, 20, 30])

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll.insert(1, 20)
        ll.insert(2, 30)
        self.assertEqual(list(ll), [10, 20, 30])

    def test_insert_index_out_of_range(self):
        ll = LinkedList()
        with self.assertRaises(IndexError):
            ll.insert(1, 10)

    def test_getitem_valid(self):
        ll = LinkedList()
        ll.insert(0, 100)
        ll.insert(1, 200)
        self.assertEqual(ll[0], 100)
        self.assertEqual(ll[1], 200)

    def test_getitem_out_of_range(self):
        ll = LinkedList()
        with self.assertRaises(IndexError):
            _ = ll[0]

    def test_getitem_negative_index(self):
        ll = LinkedList()
        ll.insert(0, 10)
        with self.assertRaises(IndexError):
            _ = ll[-1]

    def test_getitem_slice_raises(self):
        ll = LinkedList()
        with self.assertRaises(TypeError):
            _ = ll[0:1]

    def test_setitem_valid(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll[0] = 99
        self.assertEqual(ll[0], 99)

    def test_setitem_slice_raises(self):
        ll = LinkedList()
        with self.assertRaises(NotImplementedError):
            ll[0:1] = [1, 2]

    def test_delitem_raises(self):
        ll = LinkedList()
        with self.assertRaises(NotImplementedError):
            del ll[0]

    def test_iteration(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.insert(len(ll), v)
        self.assertEqual(list(ll), [1, 2, 3])

    def test_len_after_operations(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        ll.insert(0, 10)
        self.assertEqual(len(ll), 1)
        ll.insert(1, 20)
        self.assertEqual(len(ll), 2)
        ll.insert(1, 15)
        self.assertEqual(len(ll), 3)

    def test_reversed_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.reversed(), [])

    def test_reversed_single_element(self):
        ll = LinkedList()
        ll.insert(0, 10)
        self.assertEqual(ll.reversed(), [10])

    def test_reversed_multiple_elements(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll.insert(1, 20)
        ll.insert(2, 30)
        self.assertEqual(ll.reversed(), [30, 20, 10])

    def test_reversed_does_not_modify_original(self):
        ll = LinkedList()
        for v in [10, 20, 30]:
            ll.insert(len(ll), v)
        ll.reversed()
        self.assertEqual(list(ll), [10, 20, 30])

    def test_reverse_empty(self):
        ll = LinkedList()
        ll.reverse()
        self.assertEqual(list(ll), [])
        self.assertEqual(len(ll), 0)

    def test_reverse_single_element(self):
        ll = LinkedList()
        ll.insert(0, 10)
        ll.reverse()
        self.assertEqual(list(ll), [10])
        self.assertEqual(len(ll), 1)

    def test_reverse_multiple_elements(self):
        ll = LinkedList()
        for v in [10, 20, 30]:
            ll.insert(len(ll), v)
        ll.reverse()
        self.assertEqual(list(ll), [30, 20, 10])
        self.assertEqual(len(ll), 3)

    def test_clone_empty(self):
        ll = LinkedList()
        cloned = ll.clone()
        self.assertEqual(list(cloned), [])
        self.assertEqual(len(cloned), 0)
        self.assertIsNot(cloned, ll)

    def test_clone_multiple(self):
        ll = LinkedList()
        for v in [10, 20, 30]:
            ll.insert(len(ll), v)
        cloned = ll.clone()
        self.assertEqual(list(cloned), [10, 20, 30])
        self.assertEqual(len(cloned), 3)
        self.assertIsNot(cloned, ll)


if __name__ == "__main__":
    unittest.main()