shopping_list = ["apples", "bread", "milk", "cheese"]
item_found = True

while not item_found:
  item = input("Search for an item in your list (or 'q' to quit): ")
  if item.lower() == "q":
    break  # Exit the loop if user enters 'q'
  if item in shopping_list:
    item_found = False
    print(f"{item} is on your shopping list.")
  else:
    print(f"{item} is not on your list.")