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
