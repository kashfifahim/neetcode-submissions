class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_anagram = {}

        for word in strs:
            sorted_char = str(sorted(word))
            if sorted_char in dict_anagram:
                dict_anagram[sorted_char].append(word)
            else:
                dict_anagram[sorted_char] = [word]

        return list(dict_anagram.values()) 
        