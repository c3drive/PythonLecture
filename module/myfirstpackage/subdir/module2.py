from .module3 import myfunc3
# from ..subdir import module3
from .. import module1
def myfunc():
    print("This is module2")

def myfunc2():
    print("This is module2 from mydunc2")
    myfunc3()
    # module3.myfunc3()
    module1.myfunc()