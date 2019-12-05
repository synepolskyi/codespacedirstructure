class MyClass:

    def __new__(cls, *args, **kwargs):
        
        if set(args).issubset({'A', 'B'}):
            return super().__new__(cls)

        return super().__new__(object)


mc1 = MyClass('A')
mc2 = MyClass('A','B')
not_mc1 = MyClass('C')
not_mc2 = MyClass('B','C')

print(type(mc1))
print(type(mc2))
print(type(not_mc1))
print(type(not_mc2))