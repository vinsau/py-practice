dict1 = {"John": 25, "Alice": 30, "Bob": 22}
dict2 = {"Eve": 28, "Charlie": 35, "David": 40}

merge_dict = {}

for data in dict1:
    merge_dict[data] = dict1[data]

for data in dict2:
    merge_dict[data] = dict2[data]

print(merge_dict)