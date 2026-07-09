def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

arr = [1,2,3,4,7,6,5,4,3,2,1]
print(selection_sort(arr))

# Best: O(n²)
# Average: O(n²)
# Worst: O(n²)
#
# Space: O(1) (in-place)