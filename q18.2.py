import array

arr = array.array('i', [10, 20, 30, 40, 50])
print(f"Array contains {len(arr)} elements. Valid indices are 0 to {len(arr) - 1}.")

while True:
    index = input("Enter the index to retrieve the element (-1 to quit): ")
    if index == "-1":
        print("Exiting the program.")
        break
    try:
        index = int(index)
        if 0 <= index < len(arr):
            print(f"Element at index {index}: {arr[index]}")
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

