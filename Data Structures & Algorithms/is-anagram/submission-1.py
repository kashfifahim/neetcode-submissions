class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if the two strings are the same size
        if len(s) != len(t):
            return False
        else:
            sorted_s = sorted(s)
            sorted_t = sorted(t)
            for index, char in enumerate(sorted_s):
                if sorted_s[index] != sorted_t[index]:
                    return False
        return True