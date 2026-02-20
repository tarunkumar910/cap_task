# Question 7: Count occurrences of a specific digit in a number

a = 122342222

target = int(input("enter the digit to count"))
total = 0

while a != 0:
    digit = a % 10
    if digit == target:
        total = total + 1
    
    a = a // 10

print(total, "times target digit appears")
