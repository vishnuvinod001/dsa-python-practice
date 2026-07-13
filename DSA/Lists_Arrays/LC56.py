def mergeIntervals(intervals):
    intervals.sort()
    
    ans = [intervals[0]]
    
    for start, end in intervals[1:]:
        
        last_end = ans[-1][1]
        
        if start <= last_end:
            ans[-1][1] = max(last_end, end)
        
        else:
            ans.append([start, end])
    
    return ans

arr = [[1,4], [3,5], [4,7], [6,10], [11,12], [13,17], [12, 20]]
print(mergeIntervals(arr))

ans = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(ans))

"""
    
* Start with the 1st interval array (intervals[0]). Store this to "ans" array
* Start iteration from the 2nd element of intervals.
* ans[-1][1] => this gives the last element of the latest interval in "ans". => this is stored to last_end.
* just iterate through each nested array, if the start of the nested array is less than the last_end, make the last element of the latest interval appended into "ans", the max of end and last_end. => interval merged!
* return the "ans" array with the merged intervals.


"""