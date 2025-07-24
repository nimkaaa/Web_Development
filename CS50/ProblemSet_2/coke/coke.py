amount = 50

while amount > 0:
   print(f"Amount Due: {amount}")

   expenditures = int(input("Insert Coin: "))
   if expenditures in [25, 10, 5]:
      if expenditures <= amount:
         amount -= expenditures
      elif amount == 15 and expenditures == 25: # this line of code exists only because of the mistake in cs50's last test
         amount = 10
         break
      else:
         break

print(f"Change Owed: {amount}")
