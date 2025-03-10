from inspect import getgeneratorlocals, getgeneratorstate


def sub_gen():
    try:
        print('inside sub_gen')
        yield 1
        yield 2
        yield 3
    finally:
        print("finally sug_gen closed")
        return "Return value from subgen when closing" # it with return a value to StopIteration Exception


def delegator():
    print('start delegator')
    s = sub_gen()
    print('before yielding')
    result = yield from s
    print('result of sub_gen:', result)
    yield "delegator: subgen closed"
    print("delegator closing...")
    return "Return value from gen when closing" # it with return a value to StopIteration Exception



d = delegator()
print('delegator created')
next(d)
print(getgeneratorlocals(d))

print('delegator_state', getgeneratorstate(d))
#print('sub_gen_state', getgeneratorstate(sub))

try:
    print('1:',next(d))
    print('2:',next(d))
    print('3:',next(d))
    print('4:',next(d))
except StopIteration as ex:
    print("Exception:", ex.value)


print('delegator_state', getgeneratorstate(d))


# OUTPUT
#
# delegator created
# start delegator
# before yielding
# inside sub_gen
# {'s': <generator object sub_gen at 0x000001F19DC3FED0>}
# delegator_state GEN_SUSPENDED
# 1: 2
# 2: 3
# finally sug_gen closed
# result of sub_gen: Return value from subgen when closing
# 3: delegator: subgen closed
# delegator closing...
# Exception: Return value from gen when closing
# delegator_state GEN_CLOSED
#
#
#
#
