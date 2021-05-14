lang = ['Java', 'C#', 'Python', 'JavaScript']
vers = [16, 9, 3.9]

# for idx, n in enumerate(lang):
#     print(f"{n:10} {vers[idx]}")

for n, v in zip(lang, vers):
    print(f"{n:10} {v}")
