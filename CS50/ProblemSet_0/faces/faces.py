def convert(str):
   str = str.replace(":)", "🙂").replace(":(", "🙁")
   return str

def main():
   text = input()
   print (convert(text))

main()
