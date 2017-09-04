class Foo(object):
    def __init__(self, s):
        # type: (str) -> None
        self.s = s

def unused_func():
    f = Foo(10) # <= 検出されない

if False:
    f = Foo(10) # <= 検出されない