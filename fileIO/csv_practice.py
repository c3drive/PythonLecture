import csv


with open("example.csv") as f:
    # 不便
    # print(f.read())

    # csv.reader(f)
    reader = csv.reader(f)
    for line in reader:
        print(line[1])

# csv.DictReader(f)
with open("example.csv") as f:
    reader = csv.DictReader(f)
    for line in reader:
        print(line)
        print(line['First Name'])

# csv.writer(f)
with open("sample.csv", mode='w') as f:
    writer = csv.writer(f)
    writer.writerow((['value1', 'value2']))
    writer.writerow(['value3', 'value4'])

# 基本的には、Dictionallyを使った方が良い
# csv.DictWriter(f)
with open("sample.csv", mode='w') as f:
    writer = csv.DictWriter(f, ['col1', 'col2'])
    writer.writeheader() # headerは['col1', 'col2']
    writer.writerow({'col1': 'value1', 'col2': 'value2'})
    writer.writerow({'col1': 'value3', 'col2': 'value4'})

