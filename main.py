import pyglet


def tag(n):
    def fooDecor(fn):
        def wrapper(*args, **kwargs):
            fn(*args, **kwargs)
            print("Finished Wrapper")
            print(f"Prefix Arg: {n}")
        return wrapper
    return fooDecor

@tag('Boobies')
def hello(a):
    print("Hello Function")


hello(1)
print("Done")
