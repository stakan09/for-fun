def deco(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        print('This is made by decorator function.')
    return wrapper

class XXX:
    def __init__(self,acts):
        self.acts=acts

    @deco
    def comments(self):
        print(self.acts)

somebody = XXX('This is a value of somebody')
somebody.comments()