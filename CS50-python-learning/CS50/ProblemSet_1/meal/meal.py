def main():
    user = input("What time is it? ")
    user = convert(user)
    
    if 7.0 <= user <= 8.0:
        print("breakfast time")
    elif 12.0 <= user <= 13.0:
        print("lunch time")
    elif 18.0 <= user <= 19.0:
        print("dinner time")



def convert(time):
    hours, minutes = time.replace(":", " ").split()

    hours = float(hours)
    minutes = float(minutes)

    minutes = round(minutes / 60, 2)
    
    return hours + minutes


if __name__ == "__main__":
    main()
