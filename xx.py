def decorator(func):
    def wrapper():
        print('perform before fn call')
        func()
        print('perform after fn call')
    return wrapper

@decorator
def say_hello():
    print('hey')
say_hello()

