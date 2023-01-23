import random
list = []
def swap(a, b):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list
for i in range(10):
    list.append(int(random.randint(1,100)))
print("The unsorted list is: ", end='')
print(list)
for i in range(len(list)):
    min = i
    for j in range(len(list)-i):
        if list[j] < list[min]:
            min = j
    if min != i:
        swap(list[i], list[min])
print("The sorted list is: ", end='')
print(list)