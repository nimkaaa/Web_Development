#
# 1. Ask user for an amount of mass
# 2. Calculating result with E = mc^2
# 3. Printing result
#

def main():
   mass = int(input("Enter a mass: "))
   speed = 300000000
   
   Energy = mass * speed ** 2

   print(f"Energy: {Energy}")


main()