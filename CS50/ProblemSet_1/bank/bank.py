def main():
   greeting = input("Greeting: ")

   if greeting.find("Hello") == 0:
      print("$0")
   elif greeting.find("H") == 0 or greeting.find("h") == 0:
      print("$20")
   else:
      print("$100")

main()