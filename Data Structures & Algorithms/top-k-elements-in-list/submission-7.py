class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = defaultdict(int)

        for num in nums:
            result[num] = result.get(num, 0) + 1

        # now that we have the table with the numbers and the count of each number, we need to sort in descending order
        # return the first k num

        # Sort by value
        sorted_dict = dict(sorted(result.items(), key=lambda item: item[1]))

        return list(sorted_dict)[::-1][:k]
