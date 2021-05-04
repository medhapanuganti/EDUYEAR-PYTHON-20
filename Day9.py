#pattern without using loop

def pattern(a,b):
    print(a,end='')
    if a<=0:
           return
    pattern(a-b,b)
    print(a,end='')
a,b=map(int,input().split())
pattern(a,b)
print()
