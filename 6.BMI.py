height= float(input("please enter your height(m):"))
weight= float(input("please enter yor weight(kg):"))
BMI= (weight/(height*height))
if(BMI > 40):
    print(BMI , "you have level 3 obesity!")
elif (35 <= BMI <= 40):
     print(BMI , "you have level 2 obesity!")
elif(30 <= BMI < 35):
    print(BMI , "you have level 1 obesity!")
elif(24 <= BMI < 30):
     print(BMI , "you are overweight!")
elif(18.5 <= BMI < 24):
    print(BMI , "you are normal! be carefull")
elif(16 <= BMI < 18.5):
    print(BMI , "you are underweight! ")
else:
    print("try again!")


