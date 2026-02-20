# question 6

s = "hello"
if len(s) >= 5: 
    mid_char = s[len(s) // 2] 
    if mid_char.lower() in 'aeiou':
        print("Middle character is a vowel")
else:
    print("String too short")
