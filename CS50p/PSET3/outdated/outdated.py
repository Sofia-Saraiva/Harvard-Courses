months = [
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
    date = input("Date: ")

    if "," in date:
        month, day, year = date.split(" ")
        try:
            day = day.strip(',')
            day = int(day)
            index = months.index(month)
            index = int(index) + 1
            if day <= 31 and index <= 12:
                print(f"{year}-{index:02}-{day:02}")
                break
        except ValueError:
            pass
    elif "/" in date:
        month, day, year = date.split("/")
        try:
            month = int(month)
            day = int(day)
            year = int(year)
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
        except ValueError:
            pass

