import collections


class ArrayOperations:
    def __init__(self) -> None:
        pass

    def contains_duplicates(self, arr: list[int]) -> bool:
        seen = set()
        for k in arr:
            if k in seen:
                return True
            seen.add(k)
        return False

    def contains_duplicates_with_sorting(self, arr: list[int]) -> bool:
        if len(arr) <= 1:
            return False

        sorted_list = sorted(arr)
        for i in range(1, len(sorted_list)):
            if sorted_list[i - 1] == sorted_list[i]:
                return True
        return False

    # Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        diff_map: dict[int, int] = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in diff_map:
                return [diff_map[nums[i]], i]
            diff_map[diff] = i
        return []

    # Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
    # Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
    # Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
    # Return k.
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0

        front, rear = 0, len(nums) - 1

        while front < len(nums) and front < rear:
            if nums[front] == val:
                if nums[rear] == val:
                    rear -= 1
                else:
                    nums[front], nums[rear] = nums[rear], nums[front]
                    front += 1
                    rear -= 1
            else:
                front += 1

        if nums[front] == val:
            return front
        else:
            return front + 1

    def removeElement_2(self, nums: list[int], val: int) -> int:
        k = 0  # Pointer for where to write the next valid element
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1
        return k

    # Given an array nums of size n, return the majority element.
    # The majority element is the element that appears more than ⌊n / 2⌋ times in the array. You may assume that the majority element always exists in the array.
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        majority_index = {}
        for num in nums:
            majority_index[num] = majority_index.get(num, 0) + 1
            if majority_index[num] > n / 2:
                return num

        raise ValueError("No majority element")

    def majorityElementBoyerMooreVoting(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("No majority element")

        candidate, counter = nums[0], 0
        if len(nums) == 1:
            return candidate

        for num in nums[1:]:
            if num == candidate:
                counter += 1
            else:
                if counter == 0:
                    candidate = num
                else:
                    counter -= 1
        return candidate

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front, rear = 0, len(s) - 1
        while front < rear:
            s[front], s[rear] = s[rear], s[front]
            front += 1
            rear -= 1

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pass

    # sorted list
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[k] = nums[index]
                k += 1

        return k

    # valid parentheses
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        validity = {"]": "[", "}": "{", ")": "("}
        stack = collections.deque()
        for c in s:
            if c in validity:
                top = stack.pop() if stack else "#"
                if top != validity[c]:
                    return False
            else:
                stack.append(c)

        return not stack
