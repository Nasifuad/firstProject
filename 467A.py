n= int(input())
p=[]
q=[]
r=0
for i in range(n):
    p_int, q_int = map(int, input().split())
    p.append(p_int)
    q.append(q_int)

for i in range(n):
    if(q[i]-p[i]>=2):
        r+=1
        
print(r)
    
        