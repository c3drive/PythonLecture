import csv
import sys

range_nums = range(10)
for i in range_nums:
    print(i)

list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in list_nums:
    print(i)

# 全てのデータをメモリに置くことはせず、展開時（iteration時）に計算してメモリの節約を図っている
print(f"range_nums is using memor size: {sys.getsizeof((range_nums))}")

# 全てのデータをメモリにおいている
print(f"list_nums is using memor size: {sys.getsizeof((list_nums))}")

# generatorをlist化するとgeneratorの機能は失われる
generator_list_nums = list(range_nums)
print(f"generator_list_nums is using memor size: {sys.getsizeof((generator_list_nums))}")

# csv.DictReaderもgenerator
with open("example.csv") as f:
    reader = csv.DictReader(f)
    print(f"reader is using memor size: {sys.getsizeof((reader))}")

    for line in reader:
        print(line)