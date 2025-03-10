
def echo():
    output = None
    while True:
        received = yield output
        print(received[::-1])

def delegator():
    yield from echo()

e = delegator()
e.send(None)
e.send("Python")
e.send('Valet')




