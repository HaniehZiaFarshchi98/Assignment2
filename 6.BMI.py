from telnetlib import BM


height= float(input("please enter your height(m):"))
weight= float(input("please enter yor weight(kg):"))
BMI= (weight/(height*height))
if(BMI > 40):
    print(BMI , "you must go on a diet!")
elif (35 <= BMI <= 40):
     print(BMI , "you can go on a diet!")
elif(30 <= BMI < 35):
    print(BMI , "you are normal! be carefull")
elif(24 <= BMI < 30):
     print(BMI , "you ae really skinny!")
else:
    print("try again!")


