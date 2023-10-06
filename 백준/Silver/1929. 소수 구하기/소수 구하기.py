import sys
def input():  return sys.stdin.readline()

M,N = map(int,input().split())

prime = [True] *(N+1)
prime[1]=False

for i in range(2, N+1):
    for x in range(2,N+1):
        if i*x > N:
            break
        if prime[i*x]==True:
            prime[i*x]=False

for i in range(M,N+1):
    if prime[i]==True:
        print(i)