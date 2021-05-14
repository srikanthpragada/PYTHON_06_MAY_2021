lst = [10, 22, 33, 41, 34]

idx = 0
for n in lst:
    print(idx, n)
    idx += 1

for idx, n in enumerate(lst, start=1):
    print(idx, n)
