import queue
import sys
num = int(sys.stdin.readline())
Q =queue.Queue()
for i in range(num):
    sql=sys.stdin.readline().strip()
    if "push" in sql:
        x,y=list(map(str,sql.split()))
        Q.put(int(y))
    elif "pop" == sql:
        if Q.empty():
            print(-1)
        else:
            A=Q.get()
            print(A)
    elif "size" == sql:
        print(len(Q.queue))
    elif "empty" == sql:
        if Q.empty():
            print(1)
        else:
            print(0)
    elif "front" == sql:
        if Q.empty():
            print(-1)
        else:
            print(Q.queue[0])
    elif "back" == sql:
        if Q.empty():
            print(-1)
        else:
         print(Q.queue[len(Q.queue)-1])
        