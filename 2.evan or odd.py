
from math import remainder


print("please enter your number=")
number= int(input())
even_count= 0
odd_count= 0
while (number > 0):
    rem = number % 10
    if rem%2 == 0:
        even_count += 1
    else:    
        odd_count += 1
    if (even_count > odd_count):
        print("even digits are more")
    elif(odd_count > even_count):
        print("odd digits are more")
    else:
        print("odd digits are equal to even digits!")



   