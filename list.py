from collections.abc import Iterator, MutableSequence
from typing import Any, Iterable, overload


class ListNode:
    def __init__(self, data) -> None:
        self.data = data
        self.next: ListNode | None = None


class LinkedList(MutableSequence):
    def __init__(self) -> None:
        self.head: ListNode | None = None
        self.size = 0

    def __len__(self) -> int:
        return self.size

    @overload
    def __getitem__(self, index: int) -> Any: ...

    @overload
    def __getitem__(self, index: slice[Any, Any, Any]) -> MutableSequence: ...

    def __getitem__(self, index: int | slice):
        if isinstance(index, slice):
            raise TypeError("Slices are not supported in this simple list")

        if index < 0:
            raise IndexError("Negative indices are not supported")

        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError("List index out of range")
            current = current.next

        if current is None:
            raise IndexError("List index out of range")
        return current.data

    def insert(self, index: int, value: Any) -> None:
        if index < 0:
            raise IndexError("Negative indices are not supported")

        if index > self.size:
            raise IndexError("Insertion index is higher than the size of the list")

        if index == 0:
            new_node = ListNode(value)
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return

        current = self.head
        prev = current

        for _ in range(index):
            if current is None:
                break
            prev = current
            current = current.next

        if prev is not None:
            new_node = ListNode(value)
            if current is None:
                prev.next = new_node
            else:
                new_node.next = current
                prev.next = new_node
            self.size += 1

    @overload
    def __setitem__(self, index: int, value: Any) -> None: ...

    @overload
    def __setitem__(self, index: slice[Any, Any, Any], value: Iterable) -> None: ...

    def __setitem__(self, index: int | slice, value: int | Iterable):
        if isinstance(index, slice):
            raise NotImplementedError("Slice not supported in this simple list")

        if isinstance(value, Iterable):
            raise NotImplementedError("Iterables not supported in this simple list")

        self.insert(index, value)

    @overload
    def __delitem__(self, index: int) -> None: ...

    @overload
    def __delitem__(self, index: slice[Any, Any, Any]) -> None: ...

    def __delitem__(self, *args, **kwargs):
        raise NotImplementedError

    def reversed(self) -> Iterable[int]:
        if self.head is None:
            return []

        return [x.data for x in self._reverse(self.head)]

    def _reverse(self, node: ListNode | None) -> Iterator[ListNode]:
        if node is None:
            return

        yield from self._reverse(node.next)
        yield node
