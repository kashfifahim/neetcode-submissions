class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_catalog = {}
        for element in nums:
            if element in num_catalog:
                num_catalog[element] += 1
            else:
                num_catalog[element] = 1
        
        for num, frequency in num_catalog.items():
            if frequency > 1:
                return True
        
        return False
        