n = int(input())
counter = 0
for i in range(n):
    row = list(map(int,input().split()))
    for z in row:
        if z == 1:
            counter += 1
print(counter//2)