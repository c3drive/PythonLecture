class MyError1(Exception):

    def __str__(self):
        return "my erro occurred"

class MyError2(Exception):

    def __str__(self):
        return "my erro occurred"

if __name__ == "__main__":
    response = input("y/n")
    try:
        if response != "y" and response != "n":
            # raise MyError1("my erro occurred")
            raise MyError1

    except MyError1 as e:
        print(e) # e.__str__()

    # こちらの書き方が一般的
    response = input("y/n")
    if response != "y" and response != "n":
        raise MyError2