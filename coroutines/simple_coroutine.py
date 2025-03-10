import math


def coroutine(gen_fn):
    def inner(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def powerof(v):
    result = None
    while True:
        received = yield result
        result = math.pow(received, v)


sqrt = powerof(2)

print(f"2^2={sqrt.send(2)}")
print(f"2^3={sqrt.send(3)}")
print(f"2^(-5){sqrt.send(-5)}")


cube = powerof(3)

print(f"3^2={cube.send(2)}")
print(f"3^3={cube.send(3)}")
print(f"{cube.send(-4)}")


