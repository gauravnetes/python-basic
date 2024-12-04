# Method 2: Manually iterating through the array

import array

arr = array.array('i', [10, 24, 456, 5, 56])

largest = arr[0]

for num in arr:
    if num > largest: 
        largest = num

print("The largest element in the array is:", largest)
