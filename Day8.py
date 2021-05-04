#prime or not

num=int(input("enter any number"))
flag=False
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            flag=True
            break
if flag:
    print(num,"is not prime")
else:
    print(num,"is prime")




#factorial

def factorial(num):
    flag=1
    for i in range(1,num+1):
        flag=flag*i
    print("factorial of {} is {}".format(num,flag))
factorial(int(input("enter any number")))
