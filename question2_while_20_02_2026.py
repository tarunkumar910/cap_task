# Question 2: Reverse a number and compare

num = 234
temp = num
rev = 0
while temp != 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10

if rev > temp:
    print("yes")
else:
    print("no")
