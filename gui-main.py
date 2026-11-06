from tkinter import *
from tkinter import ttk
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

FORMAT_FUNCS = {name: func for name, func in FORMATS.values()}

UPDATE_MS = 2000

root = Tk(className="dragonclock")
root.title("Dragon Clock")

mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

exit = ttk.Button(mainframe, text='exit', command=root.destroy)
exit.grid(column=3, row = 0, sticky=(N, E))


formats = ttk.Combobox(mainframe, state="readonly", width=28,
                       values=[name for name, _ in FORMATS.values()])
formats.current(0)
formats.grid(column=0, row=0, sticky=(W, E))

time_label = ttk.Label(mainframe, text="")
time_label.grid(column=0, row=1, sticky=(W, E), pady=(10,0))

def update_time():
    func = FORMAT_FUNCS.get(formats.get())
    if func:
        time_label.config(text=func())
    # Reschedule itself; this returns immediately, nothing blocks
    root.after(UPDATE_MS, update_time)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
update_time()
root.mainloop()