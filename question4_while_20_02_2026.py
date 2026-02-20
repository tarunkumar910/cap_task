# Question 4: Count odd and even digits in a number

a = 46473892
odd = 0
even = 0

while a != 0:
    digit = a % 10
    if digit % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    a = a // 10

print(even)
print(odd)
