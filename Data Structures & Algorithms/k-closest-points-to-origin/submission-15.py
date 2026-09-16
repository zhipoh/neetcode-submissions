class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # try with quicksort
        # get dictionary with values storing the euclidean distance

        mp = defaultdict(list)
        for point in points:
            distance = round((((point[0]-0)**2 + (point[1]-0)**2))**(1/2),2)
            
            if mp[round(distance,2)]:
                mp[round(distance,2)].append(point)
            else:
                mp[round(distance,2)] = [point]
        
        mp = dict(sorted(mp.items(),key=lambda item: item[0]))
        final = list(mp.values())
        flat = [p for group in final for p in group]
        return flat[:k]