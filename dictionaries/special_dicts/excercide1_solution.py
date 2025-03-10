from collections import defaultdict, Counter

d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

#**a**: Using `defaultdict` objects

def merge_and_count(*data):
    result = defaultdict(lambda : 0)
    for d in  data:
        for i in d:
            result[i] += d[i]

    return dict(sorted(result.items(), key=lambda k : k[1], reverse=True))

print(merge_and_count(d1, d2, d3))



#**b**: Using `Counter` objects

def merge_and_count2(*data):
    result = Counter()
    for d in  data:
        result.update(d)

    return dict(sorted(result.items(), key=lambda k : k[1], reverse=True))

print(merge_and_count2(d1, d2, d3))



def merge_and_count3(*data, top = None):
    result = Counter()
    for d in  data:
        result.update(d)
    return dict(result.most_common(top))

print(merge_and_count3(d1, d2, d3, top =3))