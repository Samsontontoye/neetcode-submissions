class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for number in nums:
            if number in result:
                return True
            result.add(number)
        return False
        