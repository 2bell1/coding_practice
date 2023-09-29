import sys

size = int(sys.stdin.readline())
arr = []
for i in range(size):
    arr.append( sys.stdin.readline().strip())
tmpset = set(arr)
arr = list(tmpset)
arr.sort(key= lambda x : (len(x), x))

for i in range(len(arr)):
    sys.stdout.write(f"{arr[i]}\n")
