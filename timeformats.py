from datetime import datetime, timezone, timedelta
import math


def twentyfour():
    return datetime.now().strftime("%H:%M:%S")
    

def twelve():
    return datetime.now().strftime( "%I:%M:%S %p")
    

def twentryfour_date():
    now = datetime.now()
    return now.strftime("%D %H:%M:%S")
    

def twelve_date():
    now = datetime.now()
    return now.strftime("%D %I:%M:%S %p")
    

def iso():
    now = datetime.now()
    return now.isoformat()
    

def iso_date():
    now = datetime.now()
    return now.strftime("%Y-%j %H:%M")

def iso_week_date():
    now = datetime.now()
    return now.strftime("%G-W%V-%u")
    

def unix():
    now = datetime.now()
    return now.timestamp()


def jd():
    now = datetime.now()
    return now.toordinal() + 1721424.5 + (now.hour + now.minute/60 + now.second/3600) / 24
    

def sit():
    bmt = datetime.now(timezone(timedelta(hours=1)))
    time = (bmt.hour * 3600 + bmt.minute * 60 + bmt.second) / 86.4
    return f"@{time:06.2f}"
    

def frt():
    now = datetime.now()
    frac = (now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6) / 86400

    h = int(frac * 10)
    m = int(frac * 1000 % 100)
    s = int(frac * 100000 % 100)
    return f"{h}:{m:02d}:{s:02d}"
    

def hex():
    now = datetime.now()
    frac = (now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6) / 86400
    return f"{int(frac * 65536):04x}"

def bi():
    now = datetime.now()
    return f"{now.hour:06b} {now.minute:06b} {now.second:06b}"

def percent():
    now = datetime.now()
    frac = (now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6) / 86400
    return f"{frac * 100:.3f}%"

def gmst():
    now = datetime.now()
    jd = t = now.toordinal() + 1721424.5 + (now.hour + now.minute/60 + now.second/3600) / 24
    d = jd - 2451545.0
    gmst_hours = (18.697374558 + 24.06570982441908 * d) % 24
    return gmst_hours