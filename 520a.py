n= int(input())
str=list(input().lower())
count=[]

for i in range(n):
    if str[i] not in count:
        count.append(str[i])
if(len(count)>=26):
    print("YES")
else:
    print("NO")