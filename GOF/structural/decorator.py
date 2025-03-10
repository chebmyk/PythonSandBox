import time

def time_it(fn):
    def inner(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f'{fn.__name__} execution time: {int((end - start)*1000)} ms')
        return result
    return inner



def do_smth():
    print("Start do smth")
    time.sleep(1)
    print("Done!!!")



do_smth =time_it(do_smth)

do_smth()


print("============= run option 2 =====================")
#============================

@time_it
def do_smth_sec(seconds):
    print("Start do smth")
    time.sleep(seconds)
    print("Done!!!")


do_smth_sec(3)