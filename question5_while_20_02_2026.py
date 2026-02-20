# Question 5: Check if a number is palindrome

num = 23432
temp = num
rev = 0
while temp != 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10

if rev == num:
    print("palindrome")
else:
    print("not palindrome")
