import sys

A = int(sys.stdin.readline())
ans = 0

while A > 0:
    if A % 5 == 0:
        ans += A // 5
        break
    A -= 3
    ans += 1

if A < 0:
    print(-1)
else:
    print(ans)
