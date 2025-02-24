text = input("Enter string to check palindrome: ")
if text == text[::-1]:
    print("Pallindrome")
else: 
    print("Not Pallindrome")