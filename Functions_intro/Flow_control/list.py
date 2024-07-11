"""Lists Methods:
    remove(item)
    append(item)
    sort()
    pop(index)
"""

# my_list = [1, 2, 3]
# my_list.append(0)    #To add
# print(my_list)

# my_list = [1, 3, 2, 3]
# my_list.remove(3)    #To remove
# print(my_list)

# my_list = [9, 4, 1, 3, 2]
# my_list.sort()    #To order them
# print(my_list)

# my_list = [1, 2, 3, 6, 7]
# my_list.pop(2)    #To remove item from a list
# print(my_list)

# my_list = [1, 2, 3, 6, 7]
# item = my_list.pop(2)    #To remove item from a list
# print(item)    #This will show us which item is removed
# print(my_list)   #This will show us the remaining items


"""Dictionary Methods:
    keys()
    values()
    items()
    get(key)
"""

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# print(my_dict.keys())       # Prints the keys
# print(my_dict.values())     # Prints the values
# print(my_dict.items())      # Prints the items
# print(my_dict.get('b'))     # Prints the value of the key
# print(my_dict)
# print(my_dict["b"])         # This will print the values of the keys


# dictionary = {'a': 1, 'b': 2, 'c': 3}
# print(dictionary.values())       # Prints the values
# dictionary["a"] = 45             # changes the value of the key
# print(dictionary.values()) 

# my_dict = {'a': 10, 'b': 25, 'c': 31}
# print(my_dict.items())            # Prints the items

# my_dict = {'a': 32, 'b': 15, 'c': 65}
# print(my_dict.get('b'))              # Prints the value of the key

"""Set Methods:
    add(item): Add item to the set
    remove(item): Remove item from the set
    union(set): Return union of sets
    intersection(set): Return a new set that contains only the elements that are present in both
"""

# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# my_set.add(9)
# print(my_set)

# my_set = {1, 2, 3, 4, 5}
# print(my_set)
# my_set.remove(4)
# print(my_set)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# union_set = set2.union(set1)
# print(union_set)

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# intersection_set = set2.intersection(set1)
# print(intersection_set)

"""Tuple Methods:
    count(item): Return the number of occurances of item in a tuple
    index(item): Return the first index of item in a tuple
"""

# my_tuple = (1, 2, 3, 4, 2, 4, 2)
# count = my_tuple.count(2)
# print(count)

my_tuple = (1, 2, 3, 4, 2, 4, 2)
index = my_tuple.index(2)       # Index means the position of the element of the item
print(index)