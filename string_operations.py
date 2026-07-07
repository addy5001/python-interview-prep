class StringOperations:
    def __init__(self) -> None:
        pass

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen: dict[str, int] = {}
        for c in s:
            seen[c] = seen.get(c, 0) + 1

        for c in t:
            if c not in seen or seen[c] == 0:
                return False
            seen[c] -= 1

        return True

    # You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
    # Specifically, ans is the concatenation of two nums arrays.
    def getConcatenation(self, nums: list[int]) -> list[int]:
        ans = []
        n = len(nums)
        for i in range(2 * n):
            ans.append(nums[i % n])

        return ans

    # You are given an array of strings strs. Return the longest common prefix of all the strings.
    # If there is no longest common prefix, return an empty string "".
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]

        lcp = []
        min_length = min(len(item) for item in strs)

        for i in range(min_length):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    return "".join(lcp)
            lcp.append(char)

        return "".join(lcp)

    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front, rear = 0, len(s) - 1
        while front < rear:
            s[front], s[rear] = s[rear], s[front]
            front += 1
            rear -= 1

    def isPalindrome(self, s: str) -> bool:
        front, rear = 0, len(s) - 1
        while front < rear:
            while front < rear and not str.isalnum(s[front]):
                front += 1

            while front < rear and not str.isalnum(s[rear]):
                rear -= 1

            if str.upper(s[front]) != str.upper(s[rear]):
                return False
            else:
                front += 1
                rear -= 1

        return True

    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_index, w2_index = 0, 0
        merged = []

        while w1_index < len(word1) and w2_index < len(word2):
            merged.append(word1[w1_index])
            merged.append(word2[w2_index])
            w1_index += 1
            w2_index += 1

        merged.append(word1[w1_index:])
        merged.append(word2[w2_index:])

        return "".join(merged)
