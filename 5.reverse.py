print("please enter your number:")
number = int(input())
rev = 0
orig = number
while(number > 0):
    rem = number%10
    rev = rem + (rev*10)
    number= int(number/10)
if orig==rev:
    print("your number is equal to its reverse")
else:
    print("your number isn,t equal to its revers")