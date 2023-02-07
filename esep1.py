#Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
A=int(input())
B=int(input())
if(A<=B):
    for(int i=A;i<=B;i++):
        print(i)
else:
    print("ERROR")