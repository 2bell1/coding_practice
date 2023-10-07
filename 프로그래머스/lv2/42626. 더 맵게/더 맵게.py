import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    min = 0
    while scoville and min < K:
        min = heapq.heappop(scoville)
        if min < K and len(scoville)==0:
            answer=-1
            break
        elif min < K:
            min2 = heapq.heappop(scoville)
            tmp = min + (min2*2)
            heapq.heappush(scoville,tmp)
            answer+=1
        else:
            heapq.heappush(scoville,min)
    return answer