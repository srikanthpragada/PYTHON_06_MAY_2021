# default parameter
def wish(msg="Hello", name='Guest'):
    print(msg, name)


wish("Hello", "Mark")  # Positional
wish(name="Bill", msg="Hi")  # Keyword
wish("Goodbye")
wish()
