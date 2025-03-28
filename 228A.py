n=list(map(int,input().split()))

duplicate=0
for i in range(n.__len__()):
     o=0
     for j in range(i):
         if(n[i]==n[j]):
           duplicate+=1
           break

          

            
print(duplicate)