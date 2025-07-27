def main():
   monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

   while True:
      try:
         date = input("Date: ").strip()

         for month in range(12):
            if monthes[month] in date and ',' in date:
               date_list = date.replace(',', '').split(' ')
               date_list[0] = monthes.index(date_list[0]) + 1

               if int(date_list[1]) > 31 or date_list[0] > 12:
                  break

               print(f"{date_list[2]}-{date_list[0]:02}-{int(date_list[1]):02}")
               return 0

         if "/" in date:
            date_list = date.split('/')

            if int(date_list[1]) <= 31 and int(date_list[0]) <= 12:
               print(f"{date_list[2]}-{int(date_list[0]):02}-{int(date_list[1]):02}")
               return 0
         
      except ValueError:
         pass


main()