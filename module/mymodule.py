myvariable = "This is global variable"
def myfunc():
    print("This is my function")

def _anotherfunc():
    print("This is another")

if __name__ == "__main__":
    print(f"This is mymodule: {__name__}")
