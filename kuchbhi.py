def add_all(*args):          # args = tuple of all positional inputs
    return sum(args)

def show(**kwargs):          # kwargs = dict of named inputs
    for k, v in kwargs.items():
        print(k, v)

print(add_all(1, 2, 3))            # 6
show(name="Rohit", age=20)