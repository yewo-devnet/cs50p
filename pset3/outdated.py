def main():
    list = [
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
        raw = input()
        try:
            if '/' in raw:
                month, day, year = raw.split('/')
                month = int(month)
                day = int(day)
                year = int(year)
                print(f"{year}-{month:02}-{day:02}")
            else:
                month, day, year = raw.split()
                day = int(day.rstrip(','))
                month = month.title()
                if month in list:
                    m = list.index(month) + 1
                print(f"{year}-{m:02}-{day:02}")
        except ValueError:
            print("Invalid input try again")
    
if __name__ == "__main__":
    main()