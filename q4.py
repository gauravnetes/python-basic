# 3. Array Manipulations with Functions
import array

arr = array.array('i', [10, 20, 30, 40, 50])

# display the array
print("original array: ", arr)

# add an element
arr.append(60)
print("array  after appending 60: ", arr)

# Insert an Element at a Specific Position
arr.insert(4, 56)
print("Array after inserting 56 in index 4: ", arr)

# Remove an Element by Value
arr.remove(30)
print("Array after removing 30: ", arr)

#  Pop an Element by Index
popped_element = arr.pop(3)
print("Array after popping the element on index 3: ", arr)
print(popped_element)

# Find the Sum of the Elements
array_sum = sum(arr)
print("Sum of the array elements: ", array_sum)

# Find the Average of the Elements
arr_average = array_sum / len(arr)
print("The avg of elements of the array: ", arr_average)

arr.reverse()
print("reversed array: ", arr)