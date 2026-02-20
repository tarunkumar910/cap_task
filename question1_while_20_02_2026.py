# Question 1: Print numbers divisible by 10 with digit 7, and numbers between 69-80

a = 1
while a <= 100:
    if a % 10 == 7:
        print(a)
    
    if a > 69 and a < 80:
        print(a)
    a = a + 1
