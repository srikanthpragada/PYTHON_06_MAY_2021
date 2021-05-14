squares = []
for n in range(1, 11):
    squares.append(n * n)

print(squares)

# List Comprehension
squares = [n * n for n in range(1, 11)]

st = "Python"
codes = [ord(c) for c in st if c.islower()]
print(codes)
