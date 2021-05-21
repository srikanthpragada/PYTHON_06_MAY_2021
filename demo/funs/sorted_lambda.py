nums = [10, -20, 15, -43, 55, -66, 31]

# for n in sorted(nums, key=abs):
#     print(n)

names = [' Python', 'java', '  c', 'C#', '  JavaScript']
codes = ['AB123', 'BC395', 'AA393', 'XE9', 'AA999']

for n in sorted(names, key=lambda s : s.strip().lower()):
    print(n.strip())

# for n in sorted(codes, key=lambda v : int(v[2:])):
#     print(n)
