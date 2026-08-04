class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for index, number in enumerate(nums):
            needed = target - number
            if needed in lookup:
                return[lookup[needed], index]
            lookup[number] = index
        return []