from tkinter import *
from tkinter import ttk
from timeformats import twentyfour, twelve, twentryfour_date, twelve_date, iso, iso_date, iso_week_date, unix, jd, sit, frt, hex, bi, percent, gmst
from weather import hub
import os, sys

base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

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

UPDATE_MS = 50

root = Tk(className="dragonclock")
root.title("Dragon Clock")

root.tk.call('source', os.path.join(base, 'themes', 'awthemes-10.4.0', 'awdark.tcl'))
root.tk.call('source', os.path.join(base, 'themes', 'awthemes-10.4.0', 'awlight.tcl'))

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

addr_label = ttk.Label(mainframe, text="Enter the location you want the weather for:  ")
addr_label.grid(column=0, row=2, sticky=(W,E))

address = StringVar()
location = ttk.Entry(mainframe, textvariable=address)
location.grid(column=1, row=2, sticky=(W,E))

unitsel = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
unitsel.grid(column=0, row=3, sticky=(N, W, E, S))

unit_label = ttk.Label(unitsel, text="What unit do you want the temprature in:  ")
unit_label.grid(column=0, row=0,sticky=(W,E))

unit = StringVar()
f = ttk.Radiobutton(unitsel, text="fahrenheit", variable=unit, value="f")
f.grid(column=1, row=0,sticky=(W,E))
c = ttk.Radiobutton(unitsel, text="celsius", variable=unit, value="c")
c.grid(column=1, row=1, sticky=(W,E))

tz = cords = diff = elev =  time = ct = hd = None

def get_weather():
    global tz, cords, diff, elev, time, ct, hd
    addr = address.get().strip()   # use the StringVar you already made
    u = unit.get()
    if not addr or not u:
        timezone.config(text="Enter a location and pick a unit")
        return
    try:
        tz, cords, diff, elev, time, ct, hd = hub(addr, u)
    except ValueError as e:
        timezone.config(text=str(e))
        return
    timezone.config(text=tz)
    wcords.config(text=cords)
    tdiff.config(text=diff)
    welev.config(text=elev)
    wtime.config(text=time)
    wtemp.config(text=ct)
    hourly_data.config(text=hd)

weather = ttk.Button(mainframe, text="Get Weather", command=get_weather)
weather.grid(column=1, row=4, sticky=(W,E))

weatheresults = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
weatheresults.grid(column=0, row=5, sticky=(N, W, E, S))

timezone = ttk.Label(weatheresults, text="")
timezone.grid(column=0, row =0, sticky=(W,E))

wcords = ttk.Label(weatheresults, text="")
wcords.grid(column=0, row =1, sticky=(W,E))

welev = ttk.Label(weatheresults, text="")
welev.grid(column=0, row =2, sticky=(W,E))

tdiff = ttk.Label(weatheresults, text="")
tdiff.grid(column=0, row =3, sticky=(W,E))

wtime = ttk.Label(weatheresults, text="")
wtime.grid(column=0, row =4, sticky=(W,E))

wtemp = ttk.Label(weatheresults, text="")
wtemp.grid(column=0, row =5, sticky=(W,E))

hourly_data = ttk.Label(weatheresults, text="")
hourly_data.grid(column=0, row =6, sticky=(W,E))

def update_time():
    func = FORMAT_FUNCS.get(formats.get())
    if func:
        time_label.config(text=func())
    # Reschedule itself; this returns immediately, nothing blocks
    root.after(UPDATE_MS, update_time)

s = ttk.Style()
def apply_theme():
    s.theme_use(theme.get())

themesel = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
themesel.grid(column=2, row=0, sticky=(N, W, E, S))

theme = StringVar(value="awdark")
dark = ttk.Radiobutton(themesel, text="Dark", variable=theme, value="awdark", command=apply_theme)
dark.grid(column=1, row=0)
light = ttk.Radiobutton(themesel, text="Light", variable=theme, value="awlight", command=apply_theme)
light.grid(column=1, row=1)

apply_theme()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
update_time()
root.mainloop()