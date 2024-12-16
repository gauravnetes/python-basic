# Print All Even Numbers Within a Given Range

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print("Even nums in the given range: ")

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num, end=" ")