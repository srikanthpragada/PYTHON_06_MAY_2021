def extract_number(code):
    return int(code[2:])


nums = [10, -20, 15, -43, 55, -66, 31]

for n in sorted(nums, key=abs):
    print(n)

names = ['Python', 'java', 'c', 'C#', 'JavaScript']
codes = ['AB123', 'BC395', 'AA393', 'XE9', 'AA999']

for n in sorted(names, key=str.lower):
    print(n)

for n in sorted(codes, key=extract_number):
    print(n)
