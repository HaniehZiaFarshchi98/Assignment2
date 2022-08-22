from unittest import result


scores=0
wins=0
draws=0
loses=0
result=0
for i in range (8):
    print("result:" ,scores , "1:wins 2:draws 3:loses")
    result=input()
    if result == "1":
        scores +=3
    elif result == "2":
        scores +=1    
    elif result == "3":
        scores +=0
    else:
        print("enter the result again!")    