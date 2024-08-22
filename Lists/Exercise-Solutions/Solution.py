list1 = [1, 3, 5, 7, 9]

list2 = [1, 2, 4, 6, 7, 8]


new_list=list1+list2
for i in new_list:
    if i in list1 and i in list2:
        new_list.remove(i)

print(new_list)