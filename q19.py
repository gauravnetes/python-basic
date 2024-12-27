
import array

# Program to retrieve and display a range of elements from array
arr = array.array('i', [10, 20, 30, 40, 50, 60, 70])

start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

if 0 <= start < len(arr) and 0 <= end < len(arr):
    print(f"elements from index {start} to {end} are: {arr[start:end+1]}")
