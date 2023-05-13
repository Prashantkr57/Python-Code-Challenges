lst1 = ["Apple", 14, "Nokia", 5, 19]
lst2 = ["Nokia", 11, "Samsung", 14, 19]

common_list = []

for item in lst1:
    for ele in lst2:
        if item == ele:
            common_list.append(item)

print(common_list)