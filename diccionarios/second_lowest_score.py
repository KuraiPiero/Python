arr1 = {}


for x in range(int(input())):
    name = input()
    score = float(input())
    arr1[name] = score

vals = arr1.values()
second_score = sorted(list(set(vals)))[1]
second_lowest = []

for key, value in arr1.items():
    if value == second_score:
        second_lowest.append(key)

second_lowest.sort()

for name in second_lowest:
    print(name)

