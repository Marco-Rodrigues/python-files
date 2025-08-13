numbers = [1, 2, 3, 4, 50]
##1
print("\n\n#######################\n\n")

for number in numbers:
    print("Number:", number)
print("\n\n#######################\n\n")

## 2
sum = 0
for number in numbers:
    sum += number
    print("Sum of numbers:", sum)
print("\n\n#######################\n\n")   

## 3
avarege = len(numbers)
print("Average of numbers:", sum / avarege)
print("\n\n#######################\n\n")

## 4
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest number:", smallest)
print("\n\n#######################\n\n")


## 5
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print("Largest number:", largest)
print("\n\n#######################\n\n")

