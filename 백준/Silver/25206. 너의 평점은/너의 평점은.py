grade_dict = {'A+': 4.5, 'A0': 4.0, 'B+':3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
arr = []
for _ in range(20):
    input_data = input().split()
    arr.append(input_data)


sum,de = 0,0
for i,_ in enumerate(arr):
    
    if arr[i][2] in grade_dict:
        de += (float(arr[i][1]) * grade_dict[arr[i][2]])
        sum +=  float(arr[i][1])
result = de/sum

print(round(result,6))  
