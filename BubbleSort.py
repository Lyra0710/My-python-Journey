import random
list = []
for i in range(10):
    list.append(int(random.randint(1, 100)))
print("Your unsorted list is: ", end='')
print(list)
def bubble():
    for i in range(len(list) - 1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
sorted_list = bubble()
print("Your sorted list is: ", end='')
print(sorted_list)
