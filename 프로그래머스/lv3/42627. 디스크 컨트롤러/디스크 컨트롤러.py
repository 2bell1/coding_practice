import heapq

def solution(jobs):
    answer = 0
    heap = []
    start = -1
    now =0
    i=0
    while i < len(jobs):
        for a in jobs:
            if start < a[0] <= now:
                heapq.heappush(heap,[a[1],a[0]])
        if len(heap) > 0:
            A = heapq.heappop(heap) 
            start=now
            now += A[0]
            answer += (now - A[1])
            i+=1
        else:
            now +=1
            
            
    return answer//len(jobs)