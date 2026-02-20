# Question 3: Sum of digits repeatedly until single digit

a = 438
while a >= 10:
    temp = a
    rev = 0
    while temp != 0:
        rev = rev + temp % 10
        temp = temp // 10
    
    a = rev

print(a)
