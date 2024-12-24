import array

# Program to retrieve the elements of an array using their index
arr = array.array('i', [10, 20, 30, 40, 50])

index = int(input("Enter the index to retrieve the element: "))
if 0 <= index < len(arr):
    print(f"Element at index {index}: {arr[index]}")
else:
    print("Index out of range.")