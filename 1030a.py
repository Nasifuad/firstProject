n= int(input())

l= list(map(int, input().split()))
c=0;
for i in range(n):
    if(l[i]==1):
        print("Hard")
        c=1
        break

if(c==0):
    print("Easy")
