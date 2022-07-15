x = int(input())

i = 2

ans = ''
a = 0
while(i <= x):
    check = True
    for j in range(2, ((i // 2) + 1)):
        if ((i % j) == 0):
            check = False
            break
    if(check):
        ans += (str(i) + ' ')
        a += 1
    i += 1
    
ans = ans.rstrip()

print(ans)