num = int(input())
is_prime = True

for i in range(2, num):
   if num % i == 0:
      is_prime = False

if num == 1:
    print("it's number 1, which is neither prime nor composite")
elif is_prime == True:
   print("prime")
else:
   print("composite")