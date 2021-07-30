# trancatedされる： byte=0に切り詰める
with open("writing_file.txt", mode='w') as f:
    f.write("mode=w appends text\n")

# mode='a' (append): ファイルの最後尾に内容を追加
with open("writing_file.txt", mode='a') as f:
    f.write("mode=a appends text\n")

# mode='r+': 読み書きどちらも可能
with open("writing_file.txt", mode='r+') as f:
    f.write("mode=r+ appends text\n")
    print(f.read())
    f.write("This should be the last sentence.\n")
    print(f.read())


# mode='w+': 読み書きどちらも可能、Truncateされることに注意
with open("writing_file.txt", mode='w+') as f:
    print(f.read())
    f.write("mode=w+ appends text\n")
    print(f.read()) # positionが[~ appends text]の後ろにあるので何も表示されない
    f.seek(0) # positionを最初に戻す
    print(f.read())


# mode='a+': 読み書きどちらも可能で、positionが最後尾から始まる
with open("writing_file.txt", mode='a+') as f:
    print(f.read())
    f.write("mode=a+ appends text\n")
    print(f.read()) # positionが[~ appends text]の後ろにあるので何も表示されない
    f.seek(0) # positionを最初に戻す
    print(f.read())