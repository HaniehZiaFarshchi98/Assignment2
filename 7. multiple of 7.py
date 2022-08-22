from unittest import result


number=int(input("print enter your number:"))
if (number % 7 == 0):
    print("your number is multiple  of 7!")
else:
    print("your number isn't multiple of 7" ) 
    result= number + (7 - (number%7))
    print(result)