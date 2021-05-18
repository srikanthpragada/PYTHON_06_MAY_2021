# Keyword-only arguments
def wish(*, message='Hi', name ='Guest'):
    print(message, name)


wish(name='Tom')
wish(message="Hello", name="Marshall")
