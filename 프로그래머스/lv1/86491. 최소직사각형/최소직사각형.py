def solution(sizes):
    answer = 0
    w=set()
    h=set()
    
    for i,(x,y) in enumerate(sizes):
        if x> y:
            w.add(x)
            h.add(y)
        else:
            w.add(y)
            h.add(x)
    answer = max(w) * max(h)
    return answer