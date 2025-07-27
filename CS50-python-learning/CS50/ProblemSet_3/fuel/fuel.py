def main():
   tank = get_fraction()

   print_result(tank)


def get_fraction():
   while True:
      try:
         numbers = input("Fraction: ").split('/')
         x = int(numbers[0])
         y = int(numbers[1])

         if x < y:
            return round(x / y, 2)
         
      except (ValueError, ZeroDivisionError, IndexError):
         pass


def print_result(fraction):
   result = round(fraction * 100)

   if result <= 1:
      print("E")
   elif result >= 99:
      print("F")
   else:
      print(f"{result}%")


main()