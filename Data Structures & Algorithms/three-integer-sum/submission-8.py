class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use dictionary with list, capture the sum of first two values, and the value as a list of the indices.
        # sort first. run a loop. then establish l,r 
        res = []
        numsort = sorted(nums)

        for i in range(len(numsort) - 1):
            if numsort[i] > 0:
                break

            if i > 0 and numsort[i] == numsort[i-1]:
                continue

            l, r = i + 1, len(numsort)-1
            while l < r:
                threesum = numsort[i] + numsort[l] + numsort[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([numsort[i], numsort[l], numsort[r]])
                    l, r = l + 1, r - 1
                    while numsort[l] == numsort[l-1] and l < r:
                        l += 1
        return res