# Question 6: Password validation with limited attempts

p = "tarun123"

a = 1
while a <= 3:
    b = input("enter the password")
    if p == b:
        print("right password")
        break
    else:
        print("you have left login attempt", 3 - a)
    
    a = a + 1
