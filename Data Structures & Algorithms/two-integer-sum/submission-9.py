class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        i, j = 0, 0
        for i in range(len(nums)):
            partner = target - nums[i]
            print(partner, i, nums[i])
            if partner in nums:
                if nums.index(partner) == i:
                    continue
                j = nums.index(partner)
                print(i, j)
                break
        if i < j:
            result.append(i)
            result.append(j)
        else:
            result.append(j)
            result.append(i)
        return result