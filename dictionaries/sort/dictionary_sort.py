composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
#1

#Solution1
def sortit(d):
    return { k: composers[k] for k in sorted(composers, key=lambda c : composers[c]) }
print("Task1",sortit(composers))

#Solution2
def sortit2(d):
    return dict( sorted(d.items(), key=lambda c : c[1]) )
print("Task1",sortit2(composers))

#2.

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

def merge(d1, d2):
    d = {k: (d1[k], d2[k]) for k in d1.keys() & d2.keys()}
    return d
print("Task2",merge(d1,d2))


#3. Group By

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

def combine(*sources):
    result = {}
    for source in sources:
        for k in source:
            result[k] = result.get(k, 0) + source[k]
    return sortit(result)

print("Task3",combine(d1, d2))


# 4.

n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}


def load_balance(*nodes):
    union = {}
    inter = {}
    for node in nodes:
        if union:
            union |=  node.keys()
            inter &= node.keys()
        else:
            union = node.keys()
            inter = node.keys()

    result = union - inter

    return {k : tuple(n.get(k,0) for n in nodes)  for k in result }


print("Task4",load_balance(n1, n2, n3))