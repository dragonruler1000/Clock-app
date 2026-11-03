from timeformats import twentyfour, twelve, twentryfour_date, twelve_date, iso, iso_date

FORMATS = {
    "1": ("24 hour", twentyfour),
    "2": ("12 hour", twelve),
    "3": ("24 hour with date", twentryfour_date),
    "4": ("12 hour with date", twelve_date),
    "5": ("ISO format", iso),
    "6": ("ISO date", iso_date)
}
loop = 1

while loop >= 1:
    print("Advalible formats:")
    for key, (name, _) in FORMATS.items():
        print(f"{key}: {name}")

    choice = input("What time format do you prefer or q to quit: ")
    if choice in FORMATS:
        name, func = FORMATS[choice]
        func()
    elif choice == "q":
        loop = 0
    else:
        print("Invalid choice")
