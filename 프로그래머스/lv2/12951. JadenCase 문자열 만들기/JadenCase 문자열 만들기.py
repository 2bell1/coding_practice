def solution(s):
    answer = ''
    part = s.split(" ")
    print(len(part))
    for i in range(len(part)):
      answer+=part[i].capitalize()
      if i != (len(part)-1):
            answer += " "
    
    return answer