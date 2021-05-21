def extract_alpha(word_str):
    new_word = ''
    for c in word_str:
        if c.isalpha():
            new_word += c

    return new_word


words = ['Ab12c', 'x12y2', 'sdfds33&']

for word in map(extract_alpha, words):
    print(word)
