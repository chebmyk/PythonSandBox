from inspect import getgeneratorstate


def subgen():
    yield 1
    yield 2

def gen_with_subgen():
    yield from subgen()
    yield "Done"


gen = gen_with_subgen()

print('Gen state before', getgeneratorstate(gen))

for i in gen:
    print('Gen state in loop', getgeneratorstate(gen))
    print(i)


print('Gen state after', getgeneratorstate(gen))

#try call generator after it closed
next(gen)