def extract_number(code):
    print("Code :",code)
    return int(code[2:])


nums = [10, -20, 15, -43, 55, -66, 31]

# for n in map(abs, nums):
#     print(n)

names = ['Python', 'java', 'c', 'C#', 'JavaScript']
codes = ['AB123', 'BC395', 'AA393', 'XE9', 'AA999']

numbers = map(extract_number, codes)
print(numbers)

for n in numbers:
    print(n)
