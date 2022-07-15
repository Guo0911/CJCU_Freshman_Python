x = int(input())

i = 1

ans = ''

while(i <= x):
    if ((i % 3) == 0):
        ans += (str(i) + ' ')
    i += 1
ans = ans.rstrip()

print(ans)