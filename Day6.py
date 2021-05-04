#index values of vowels
str=input("enter a string")
for i in range(0,len(str)):
    if(str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u'):
        print(i,end="")





#reverse the words of a string

s=input("\n enter a string")
a=s.split()
a=a[::-1]
rev=''.join(a)
print(rev)




#remove duplicate elements without using set()

x=list(map(int,input("\n enter the numbers:").split()))
y=[]
for i in range(len(x)):
    if x[i] not in y:
        y.append(x[i])
print(y)
