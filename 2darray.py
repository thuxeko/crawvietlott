import numpy as np
import json
import itertools

# Khởi tạo mảng một chiều với kiểu dữ liệu các phần tử là Integer
arr = np.full((46,46),0)
data = None
# Load Ky
with open('lst645.json') as json_file:
      data = json.load(json_file)

for x in data:
    lstResult = x
    lstToHop = list(itertools.combinations(lstResult,2))

    for x in lstToHop:
        arr[x[0]][x[1]] += 1
        arr[x[1]][x[0]] += 1

lists = arr.tolist()
with open('teto.json', 'w') as outfile:
    json.dump(lists, outfile)