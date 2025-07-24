def main():
   grocery_list = []
   while True:
      new_item = input()
      if new_item == '':
         break
      grocery_list.append(new_item)
      grocery_list.sort()
   
   # for the first element of grocery list
   print(f"{grocery_list.count(grocery_list[0])} {grocery_list[0].upper()}")
   previous_item = grocery_list[0]

   for item in grocery_list:
      if item == previous_item:
         pass
      else:
         print(f"{grocery_list.count(item)} {item.upper()}")
      previous_item = item


main()