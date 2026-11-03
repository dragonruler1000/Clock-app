from datetime import datetime, timezone, timedelta

now = datetime.now()
dt = datetime.now(timezone(timedelta(hours=0, minutes=0)))

def twentyfour():
    t = now.strftime("%H:%M:%S")
    utc = dt.strftime("%H:%M:%S")
    print("Local: " + t)
    print("UTC-0: " + utc)  

def twelve():
    t = datetime.strftime(now, "%I:%M:%S %p")
    utc = datetime.strftime(dt, "%I:%M:%S %p")
    print("Local: " + t)
    print("UTC-0: " + utc)

def twentryfour_date():
    t = now.strftime("%D %H:%M:S")
    utc = dt.strftime("%D %H:%M:S")
    print("Local: " + t)
    print("UTC-0: " + utc)

def twelve_date():
    t = now.strftime("%D %I:%M:S %p")
    utc = dt.strftime("%D %I:%M:S %p")
    print("Local: " + t)
    print("UTC-0: " + utc)

def iso():
    t = now.isoformat()
    utc = dt.isoformat()
    print("Local: " + t)
    print("UTC-0: " + utc)

def iso_date():
    t = now.strftime("%Y-%j %H:%M")
    utc = dt.strftime("%Y-%j %H:%M")
    print("Local: " + t)
    print("UTC: "+ utc)
