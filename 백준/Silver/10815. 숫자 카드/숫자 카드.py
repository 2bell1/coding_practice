import sys

N = int(sys.stdin.readline())
N_ls = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_ls = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if M_ls[i] in N_ls:
        print("1", end=" ")
    else:
        print("0", end=" ")
