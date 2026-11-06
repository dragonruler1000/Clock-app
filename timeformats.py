from datetime import datetime, timezone, timedelta
import math

now = datetime.now()
bmt = datetime.now(timezone(timedelta(hours=1)))
frac = (now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6) / 86400

def twentyfour():
    t = str(now.strftime("%H:%M:%S"))
    return(t)

def twelve():
    t = str(datetime.strftime(now, "%I:%M:%S %p"))
    return(t)

def twentryfour_date():
    t = str(now.strftime("%D %H:%M:%S"))
    return(t)

def twelve_date():
    t = str(now.strftime("%D %I:%M:%S %p"))
    return(t)

def iso():
    t = str(now.isoformat())
    return(t)

def iso_date():
    t = str(now.strftime("%Y-%j %H:%M"))
    return(t)

def iso_week_date():
    t = str(now.strftime("%G-W%V-%u"))
    return(t)

def unix():
    t = str(now.timestamp())
    return(t)

def jd():
    t = str(now.toordinal() + 1721424.5 + (now.hour + now.minute/60 + now.second/3600) / 24)
    return(t)

def sit():
    time = (bmt.hour * 3600 + bmt.minute * 60 + bmt.second) / 86.4
    t = str(f"@{t:06.2f}")
    return(t)

def frt():
    h = int(frac * 10)
    m = int(frac * 1000 % 100)
    s = int(frac * 100000 % 100)
    t = str(f"{h}:{m:02d}:{s:02d}")
    return(t)

def hex():
    t = str(f"{int(frac * 65536):04x}")
    return(t)

def bi():
    t = str(f"{now.hour:06b} {now.minute:06b} {now.second:06b}")
    return(t)

def percent():
    t = str(f"{frac * 100:.3f}%")
    return(t)

def gmst():
    jd = t = now.toordinal() + 1721424.5 + (now.hour + now.minute/60 + now.second/3600) / 24
    d = jd - 2451545.0
    gmst_hours = (18.697374558 + 24.06570982441908 * d) % 24
    t = str(gmst_hours)
    return(t)