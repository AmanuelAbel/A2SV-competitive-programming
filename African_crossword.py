from collections import defaultdict
n,m = input().split()
n = int(n)
m = int(m)
arr = []
for i in range(n):
    a = input()
    arr.append(a)
    
ans = ""

for i in range(n):
    for j in range(m):
        letter = arr[i][j]
        count = arr[i].count(letter)
        flag = True
        for k in range(n):
            if k != i:
                if arr[k][j] == letter:
                    flag = False
        if flag and count == 1:
            ans+=letter
        

print(ans)
        
        
    