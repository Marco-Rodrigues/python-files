number = [1, 2, 3, 4, 50]

find = input("Enter a number to find: ")

for num in number:
    if str(num) == find:
        print("Number found:", num)
        break
    else:
        print("Number not found:", find)


