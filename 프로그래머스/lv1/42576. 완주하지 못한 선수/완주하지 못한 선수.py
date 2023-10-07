def solution(participant, completion):
    answer = ''
    p={}
    c={}
    for i,item in enumerate(participant):
        if item in p:
            p[item]+=1
        else:
            p[item]=1
    for i,item in enumerate(completion):
        if item in c:
            c[item]+=1
        else:
            c[item]=1
    
    for i,item in enumerate(p):
        if item in c:
            if (p[item]!=c[item]):
                answer = item
        else:
            answer=item
                
    return answer