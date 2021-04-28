a=[1,2,3,4,5,1,66]

#count even and odd numbers
P=0
Q=0
for i in range(0,len(a)):
      if a[i]%2==0:
        P+=1
      else:
        Q+=1
print("count of even and odd numbers are {},{} respectively".format(P,Q))

    
#max and min of list
max=a[0]
min=a[0]
for i in range(1,len(a)):
    if min>a[i]:
        min=a[i]
    if max<a[i]:
        max=a[i]
print("max:{} and min:{}".format(max,min)) 


#check whole list is palindrome or not
if a[::1]==a[::-1]:
      print("palindrome")
else:
      print("not a palindrome")



#print numbers those are palindrome in the list
for i in range(len(a)):
      rev_num=0
      num=a[i]
      while(num>0):
            rev_num=rev_num*10+num%10
            num=num//10
     if(rev_num==a[i]):
            print("palindrome number is {} ".format(rev_num))




