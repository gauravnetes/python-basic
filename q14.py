#  Check if a String is Palindrome

string = input("Enter a string: ")

if string == string[::-1]:
    print(f"{string} is pallindrome")
else: 
    print(f"{string} is not pallindrome")