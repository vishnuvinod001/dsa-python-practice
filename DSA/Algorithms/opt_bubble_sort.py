def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        swapped = False
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            
        if not swapped:
            break
        
    return arr

arr = [5,6,4,3,2,9,3,1]
print(bubble_sort(arr))


# (n - i - 1) => each pass the largest gets sorted, so in the next pass no need to pass till that.
# if at any point the arr is sorted => (no swap) => break and come out of the loop (stop exec)