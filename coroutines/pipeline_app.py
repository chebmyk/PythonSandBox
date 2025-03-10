import math

def coroutine(corfn):
    def inner(*args, **kwargs):
        gen = corfn(*args, **kwargs)
        next(gen)
        return gen
    return inner

@coroutine
def handle_data():
    while True:
        received = yield
        print(received)

@coroutine
def power_up(n, next):
    while True:
        received = yield
        output = math.pow(received, 2)
        next.send(output)


print_data = handle_data()

# gen = power_up(2, print_data)

# for i in range(5):
#     gen.send(i)

# outout
#
# 1.0
# 4.0
# 9.0
# 16.0


@coroutine
def filter_even(next_gen):
    while True:
        received = yield
        if received % 2 ==0:
            next_gen.send(received)

filtered = filter_even(print_data)
sqrt_gen =power_up(2, filtered)
cube_gen = power_up(3, sqrt_gen)


for i in range(1,6):
    cube_gen.send(i)



