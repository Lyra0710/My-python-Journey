# Inserting a card in a list of sorted cards

# Using the sorted function
import random
list = []
for i in range(10):
    list.append(int(random.randint(0, 100)))  # Creating a random list
sorted_list = sorted(list)  # Sorting the list using in-built function sorted which returns a sorted list of the specified iterable object
print("The set of cards is: ", end='')
print(sorted_list)
print("Enter the value of the card to be inserted: ", end='')
card = int(input())
for i in sorted_list:
    if card == sorted_list[i]:
        print("The card is already present")
sorted_list.append(card)
print("\nThe new list is: ", end='')
print(sorted(sorted_list))