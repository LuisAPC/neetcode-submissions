class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # O(n)
        res = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append([start, end])
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        
        res.append(newInterval)
        return res

