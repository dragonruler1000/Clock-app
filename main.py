from timeformats import twentyfour, twelve, twentryfour_date, twelve_date, iso, iso_date, iso_week_date, unix, jd, sit, frt, hex, bi, percent, gmst

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
loop = 1

while loop >= 1:
    print("Advalible formats:")
    for key, (name, _) in FORMATS.items():
        print(f"{key}: {name}")

    print()
    choice = input("What time format do you prefer or q to quit: ")
    print()
    if choice in FORMATS:
        name, func = FORMATS[choice]
        func()
        print()
    elif choice == "q" or "Q":
        loop = 0
    else:
        print("Invalid choice")
        print()