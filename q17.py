# Program to retrieve elements from a 2D array and display them using a for loop
arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Defining a 2D array (list of lists)

# Outer loop to iterate through each row in the 2D array
for row in arr_2d:
    # Inner loop to iterate through each element in the current row
    for element in row:
        print(element, end=" ")  # Print the element, with a space between elements
    print()  # Newline after printing all elements in the current row
