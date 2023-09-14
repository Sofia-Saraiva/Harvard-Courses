import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hours = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if hours:
        time = hours.groups()
        if int(time[1]) > 12 or int(time[5]) > 12:
            raise ValueError
        if time[2] or time[6]:
            if int(time[2]) > 59 or int(time[6]) > 59:
                raise ValueError
        t1 = convert_time(time[1], time[2], time[3])
        t2 = convert_time(time[5], time[6], time[7])
        return f"{t1} to {t2}"
    else:
        raise ValueError

def convert_time(hour, minute, ampm):
    if ampm == "PM":
        if int(hour) == 12:
            newhour = 12
        else:
            newhour = int(hour) + 12
    else:
        if int(hour) == 12:
            newhour = 0
        else:
            newhour = int(hour)
    if minute == None:
         newminute = "00"
         new = f"{newhour:02}" + ":" + newminute
    else:
        new = f"{newhour:02}:{minute}"
    return new




if __name__ == "__main__":
    main()