# 1.	Array Operations (Element-wise addition and multiplication)

import array; 

arr1 = array.array('i', [1, 2, 3, 4, 5]) # creates an array of type i
arr2 = array.array('i', [5, 4, 3, 2, 1])

sum_array = array.array('i', [arr1[i] + arr2[i] for i in range(len(arr1))])
product_array = array.array('i', [arr1[i] * arr2[i] for i in range(len(arr1))])

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Element-wise addition:", sum_array)
print("Element-wise multiplication:", product_array)

