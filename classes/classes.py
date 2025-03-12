class MyClass:
    language = 'Python'


my = MyClass()

print('Class dict:', MyClass.__dict__)
print('Instance:', my.__dict__)


print('Class property:', MyClass.language)
print('Instance property:', my.language)