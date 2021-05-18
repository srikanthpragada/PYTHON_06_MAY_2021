# Positional-only parameters 
def wish(message, name, /):
    print(message, name)


wish("Hello", "Mark")          # Positional
# wish(name="Bill", msg="Hi")    # Keyword


