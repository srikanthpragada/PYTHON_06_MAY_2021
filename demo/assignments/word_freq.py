
st = "How are you? Hope    you are    doing fine"
words = [w for w in st.split(" ") if len(w) > 0]
for w in set(words):
    print(f"{w} - {words.count(w)}")

