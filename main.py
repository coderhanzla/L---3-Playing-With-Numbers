number = int(input("Enter your Number : "))
og_num = number
rev_num = 0

while number > 0:
    digit = number % 10
    rev_num = rev_num * 10 + digit
    number = number // 10

if og_num == rev_num :
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
    
