from timeformats import twentyfour, twelve, twentryfour_date, twelve_date, iso, iso_date, iso_week_date, unix, jd, sit, frt, hex, bi, percent, gmst
from weather import hub

FORMATS = {
    "1": ("24 hour", twentyfour),
    "2": ("12 hour", twelve),
    "3": ("24 hour with date", twentryfour_date),
    "4": ("12 hour with date", twelve_date),
    "5": ("ISO format", iso),
    "6": ("ISO date", iso_date),
    "7": ("ISO week date", iso_week_date),
    "8": ("Unix time", unix),
    "9": ("Julian Day number", jd),
    "10": ("Swatch Internet Time (.beats)", sit),
    "11": ("French Revolutionary Time", frt),
    "12": ("Hexadecimal", hex),
    "13": ("Binary", bi),
    "14": ("Percent-of-day", percent),
    "15": ("Greenwich Mean Sidereal Time", gmst)
}

def clock():
     while True:
            print("Advalible formats:")
            for key, (name, _) in FORMATS.items():
                print(f"{key}: {name}")
    
            print()
            choice = input("What time format do you prefer or q to go back: ")
            print()
            if choice in FORMATS:
                name, func = FORMATS[choice]
                t =func()
                print(t)
                print()
            elif (choice == "q" or choice == "Q"):
                break
            else:
                print("Invalid choice")
                print()

def weather():
    address = input("Where do you want the weather for. eg Athens, AL: ")
    unit= input("What tempature uint do you prefer (f or c):")
    tz, cords, diff, elev, time, ct, hd = hub(address, unit)
    print("Timezone: ", tz)
    print(cords)
    print(diff)
    print(elev)
    print(time)
    print(ct)
    print("\nHourly data\n",hd)
Modes = {
    "1": ("Clock", clock),
    "2": ("Weather", weather)
}

loop = 1

while loop >= 1:
    print("Modes:")
    for key, (name, _) in Modes.items():
        print(f"{key}: {name}")
    print()
    option = input("What mode do you want to use or q to quit: ")
    print()
    if option in Modes:
        name, func = Modes[option]
        func()
        print()
    elif (option == "q" or option == "Q"):
        loop = 0
    else:
        print("Invalid choice")
        print()