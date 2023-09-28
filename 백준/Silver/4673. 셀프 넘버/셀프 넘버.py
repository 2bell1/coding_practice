natural = set(range(1, 10001))
gen = set()

for i in range(1,10001):
    for j in str(i):
        i += int(j)
    gen.add(i)

self_num= sorted(natural-gen)
for i in self_num:
    print(i)