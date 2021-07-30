# try:
#     f = open("pep8_introduction.txt")
#     for line in f:
#         # すでにファイルに改行が入っているのでprintデフォルトは改行が余計
#         # print(line) # print(line, end="¥n")
#         print(line, end="")
# finally:
#     f.close()

# with statement(勝手にcloseしてくれる）
with open("pep8_introduction.txt") as f:
    for line in f:
        print(line, end="")