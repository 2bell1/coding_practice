from collections import deque
import sys
num = int(sys.stdin.readline())
Q =deque()
for i in range(num):
    sql=sys.stdin.readline().strip()
    if "push_front" in sql:
        x,y=list(map(str,sql.split()))
        Q.appendleft(y)
    elif "push_back" in sql:
        x,y=list(map(str,sql.split()))
        Q.append(y)
    elif "pop_front" == sql:
        if len(Q) == 0:
            print(-1)
        else:
           print(Q.popleft())
    elif "pop_back" == sql:
        if len(Q) == 0:
            print(-1)
        else:
            print(Q.pop())
    elif "size" == sql:
        print(len(Q))
    elif "empty" == sql:
        if len(Q) == 0:
            print(1)
        else:
            print(0)
    elif "front" == sql:
        if len(Q) ==0:
            print(-1)
        else:
            print(Q[0])
    elif "back" == sql:
        if len(Q) ==0:
            print(-1)
        else:
            print(Q[len(Q)-1])