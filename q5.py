# 4. Modular Functions for Array/List Operations

# Display the List
def display_list(lst):
    print("Current list: ", lst)
my_list = [12, 445, 5]
display_list(my_list)

# Add an Element
def add_element(lst, element): 
    lst.append(element)
    print(f"List after adding {element}: ", lst)

add_element(my_list, 43)

#  Remove an Element by Value
def remove_element(lst, element):
    if element in lst:
        lst.remove(element)
        print(f"removed {element} from the list")
    else: 
        print(f"{element} not found in the list")

remove_element(my_list, 43)
print(my_list)

# Pop an Element by Index
def pop_element(lst, index): 
    if index < len(lst):
        popped = lst.pop(index)
        print(f"popped element at {index}: ", popped)
    else: 
        print("index out of range")

pop_element(my_list, 1)
print(my_list)