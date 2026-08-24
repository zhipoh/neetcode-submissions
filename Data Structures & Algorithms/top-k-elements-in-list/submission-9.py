class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # result = defaultdict(int)

        # for num in nums:
        #     result[num] = result.get(num, 0) + 1

        # # now that we have the table with the numbers and the count of each number, we need to sort in descending order
        # # return the first k num

        # # Sort by value in descending order
        # sorted_dict = dict(sorted(result.items(), reverse=True, key=lambda item: item[1]))

        # # convert the sorted dictionary, take the first two values
        # return list(sorted_dict)[:k]



        # # min heap (its a way to track only the top k items)
        # # A min heap helps to always keep the smallest element on top

        # # Build a frequency map
        # count = {}
        # for num in nums:
        #     count[num] = count.get(num, 0) + 1

        # # Create an empty min-heap
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, 
        #     # we are pushing a tuple for the count and their number into a heap 
        #     (count[num], num))
        #     if len(heap) > k:
        #         # remove the smallest value
        #         heapq.heappop(heap)

        # # so we have the top k value in meanheap, we just need to extract their number
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res



        # Bucket sort is the one suggested by Leetcode

        count = defaultdict(int)
        for num in nums:
            count[num] = count.get(num,0) + 1

        freq = [[] for i in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0 ,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res



