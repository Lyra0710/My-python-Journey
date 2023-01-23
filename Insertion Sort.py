import random
list = []
for i in range(10):
    list.append(int(random.randint(1, 100)))
print("Your unsorted list is: ", end='')
print(list)
for i in range(len(list)):
    key = i
    for j in range(i-1):
        while j>=0 and list[j] > key:
            list[j+1] = list[j]
            j = j-1
            list[j+1] = key

print("The sorted list is: ", end='')
print(list)