class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # count the frequency of numbers
        for number in nums:
            freq[number] = freq.get(number, 0) + 1
        # get the top k frequent elements
        result = []
        while len(result) < k:
            most_frequent = None
            highest_count = 0
            for number, count in freq.items():
                if count > highest_count:
                    highest_count = count
                    most_frequent = number
            result.append(most_frequent)
            del freq[most_frequent]
        return result