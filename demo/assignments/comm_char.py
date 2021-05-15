s1 = "Pytthoon"
s2 = "toy"

cc = set()
for c in s1:
    if c in s2 and (c not in cc):
        print(c)
        cc.add(c)
