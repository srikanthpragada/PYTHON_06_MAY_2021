st = "How do you do?"

char_freq = {c: st.count(c) for c in sorted(set(st)) if c.isalpha()}

print(char_freq)
