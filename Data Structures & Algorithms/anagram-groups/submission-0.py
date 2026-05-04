class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Get the element in the list
        # Sort that element
        # Check if it is in the dictionary
        # if it isn't add it
        # if it is, add it
        # print out the dictionary as list of list
        my_dict = {}
        for word in strs:
            print(word)
            sorted_word = "".join(sorted(word)) 
            print(sorted_word)
            print("1")
            if sorted_word in my_dict:
                print("2")
                my_dict[sorted_word].append(word)
                print("3")
            else:
                print("2b")
                my_dict[sorted_word] = [word]
                print("3b")
        print("4")
        print(my_dict)
        print("5")
        sublist = list(my_dict.values())
        print(sublist)
        return sublist


