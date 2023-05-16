class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(intervals)):

            if intervals[i][1] < newInterval[0]:
                # if cur interval starts first and is not covered by new interval
                # [cur interval]
                #                [new interval]
                # then add the cur interval in result
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                # if new interval starts first and is not covered by the cur inteval
                # [new interval]
                #                 [cur interval]
                # then add the new interval and update the new interval as cur interval
                result.append(newInterval)
                # newInterval = intervals[i]  # non pythonic way
                return result + intervals[i:]  # no need to move ahead (pythonic way)
            elif intervals[i][0] <= newInterval[1] or newInterval[0] <= intervals[i][1]:
                # if overlap
                # [cur interval]
                #       [new interval]
                # or
                # [new interval]
                #       [cur interval]
                # then merge both
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        # append the last interval
        result.append(newInterval)

        return result

