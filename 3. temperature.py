print("units: 1.c-->k   2.k-->c   3.c-->f  4.f-->c  5.f-->k  6.k-->f")
temp=float(input("please enter temperature:"))
unit=input("please select unit:")
if unit == '1':
    c_to_k = (temp + 273.15)
    print (c_to_k , "k")
elif unit == '2':
    k_to_c =(temp - 273.15)
    print (k_to_c , "c")
elif unit == '3':
    c_to_f = ((temp * 9/5) + 32)
    print (c_to_f , "f")
elif unit == '4':
     f_to_c = ((temp - 32) * 5.9)
     print (f_to_c , "c")
elif unit == '5':
    f_to_k = ((temp + 459.67)* 5/9)  
    print (f_to_k , "k")
elif unit == '6':
    k_to_f = ((temp * 9.5 ) - 459.67) 
    print (k_to_f , "f")
else :
    print ("please select again!")              
