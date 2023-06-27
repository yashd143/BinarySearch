def BinarySearch(arr, l, r, x):
 
    if r >= l:
 
        mid = l + (r - l) // 2
 
        #Middle
        if arr[mid] == x:
            return mid
 
        #Left Side
        elif arr[mid] > x:
            return BinarySearch(arr, l, mid-1, x)
 
        #Right Side
        else:
            return BinarySearch(arr, mid + 1, r, x)
 
    # Element is not present 
    else:
        return -1


arr = []
 
#number of elements as input
n = int(input("Enter number of elements : "))
 
#iterating till the range
for i in range(0, n):
    ele = int(input())
    # adding the element
    arr.append(ele) 

#sorting array
arr = sorted(arr)

#Target sequence
t = int(input("How many indexes would like to search for: "))

#Output Sequence
results = []
for _ in range(t): 
    x = int(input("Enter index to search for: "))
    result = BinarySearch(arr, 0, len(arr)-1, x)
    if result != -1:
        results.append(result)
    else:
        results.append(result)

print(results)