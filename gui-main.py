from tkinter import *
from tkinter import ttk
from timeformats import twentyfour, twelve, twentryfour_date, twelve_date, iso, iso_date, iso_week_date, unix, jd, sit, frt, hex, bi, percent, gmst

root = Tk()
root.title("Dragon Clock")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# FORMATS = {
#     "1": ("24 hour", twentyfour),
#     "2": ("12 hour", twelve),
#     "3": ("24 hour with date", twentryfour_date),
#     "4": ("12 hour with date", twelve_date),
#     "5": ("ISO format", iso),
#     "6": ("ISO date", iso_date),
#     "7": ("ISO week date", iso_week_date),
#     "8": ("Unix time", unix),
#     "9": ("Julian Day number", jd),
#     "10": ("Swatch Internet Time (.beats)", sit),
#     "11": ("French Revolutionary Time", frt),
#     "12": ("Hexadecimal", hex),
#     "13": ("Binary", bi),
#     "14": ("Percent-of-day", percent),
#     "15": ("Greenwich Mean Sidereal Time", gmst)
# }

formats = ttk.Combobox(mainframe, state="readonly", width=28)
formats['values'] = ('24 hour', '12 hour', '24 hour with date', '12 hour with date', 'ISO format', 'ISO date', 'ISO week date', 'Unix time', 'Julian Day number',
                     'Swatch Internet Time (.beats)', 'French Revolutionary Time', 'Hexadecimal', 'Binary', 'Percent-of-day', 'Greenwich Mean Sidereal Time')
formats.current(0)
formats.grid(column=0, row=0, sticky=(W, E))



root.mainloop()