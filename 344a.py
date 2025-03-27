n=int(input())
s=[]
for _ in range(n):
    s.append(input())
c=1
# 10 a new group another 10 wil be the same group 01 a new group

for i in range(n-1):
    if s[i] != s[i+1]:
        c+=1


print(c)
          

