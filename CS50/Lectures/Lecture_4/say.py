import cowsay
import sys

def main():
   if len(sys.argv) == 2:
      cowsay.dragon("hello, " + sys.argv[1])


main()