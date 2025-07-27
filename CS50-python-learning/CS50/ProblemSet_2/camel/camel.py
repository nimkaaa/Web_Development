def main():
   camel = input("camelCase: ")

   snake = ""

   for letter in camel:
      if letter.isupper():
         letter = letter.lower()
         snake += '_'
      snake += letter

   print(f"snake_case: {snake}")


main()
