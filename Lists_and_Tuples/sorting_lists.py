even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

even.extend(odd)    # Will join them
print(even)
another_even = even
print(even)

even.sort()         # Will put them in order
print(even)

even.sort(reverse=True)        # Will put them in a backward order
print(even)
print(another_even)