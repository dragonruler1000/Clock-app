from datetime import datetime, timezone, timedelta
import math

now = datetime.now()
bmt = datetime.now(timezone(timedelta(hours=1)))
frac = (now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6) / 86400

def twentyfour():
    t = now.strftime("%H:%M:%S")
    print(t)

def twelve():
    t = datetime.strftime(now, "%I:%M:%S %p")
    print(t)

def twentryfour_date():
    t = now.strftime("%D %H:%M:%S")
    print(t)

def twelve_date():
    t = now.strftime("%D %I:%M:%S %p")
    print(t)

def iso():
    t = now.isoformat()
    print(t)

def iso_date():
    t = now.strftime("%Y-%j %H:%M")
    print(t)

def iso_week_date():
    t = now.strftime("%G-W%V-%u")
    print(t)

def unix():
    t = now.timestamp()
    print(t)

def jd():
    t = now.toordinal() + 1721424.5 + (now.hour + now.minute/60 + now.second/3600) / 24
    print(t)

def sit():
    t = (bmt.hour * 3600 + bmt.minute * 60 + bmt.second) / 86.4
    print(f"@{t:06.2f}")

def frt():
    h = int(frac * 10)
    m = int(frac * 1000 % 100)
    s = int(frac * 100000 % 100)
    print(f"{h}:{m:02d}:{s:02d}")

def hex():
    print(f"{int(frac * 65536):04x}")

def bi():
    print(f"{now.hour:06b} {now.minute:06b} {now.second:06b}")

def percent():
    print(f"{frac * 100:.3f}%")

def gmst():
    jd = t = now.toordinal() + 1721424.5 + (now.hour + now.minute/60 + now.second/3600) / 24
    d = jd - 2451545.0
    gmst_hours = (18.697374558 + 24.06570982441908 * d) % 24
    print(gmst_hours)