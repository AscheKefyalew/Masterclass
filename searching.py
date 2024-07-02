shopping_list = ("milk", "pasta", "eggs", "spam", "bread", "rice")

# item_to_find = "spam"
# found_at = None   # None is a constant to show that somthing doesn't have a value

# # for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# print("Item found at poition {}".format(found_at))



# To check if the item does not exist

item_to_find = "albatros"
found_at = None   # None is a constant to show that somthing doesn't have a value

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if found_at is not None:
    print("Item found at poition {}".format(found_at))
else:
    print("{} not found")