#numbers which are divisible by 5 and 7
n,m=map(int,input("enter the range:").split())
for i in range(n,m+1):
    if i%5==0 and i%7==0:
        print(i,end=" ")


        

#sum of the series (2+22+222+...)
a='2'
terms=int(input("enter no. of terms:")
count=0
for i in range(1,terms+1):
    count+=int(a*i)
print(count)


      
#press q to quit and print sum of all numbers
total=0
while True:
    a=input("\nenter a number or press q to quit:")
    if a=='q':
        break
    total+=int(a)
print("total:",total)



#factorial of a number
S=int(input("\n\nenter a number to find factorial:"))
count=1
for i in range(1,S+1):
    count*=i
print("factorial of {} is {}".format(S,count))

