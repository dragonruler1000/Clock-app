from datetime import datetime, timezone, timedelta
now = datetime.now()
dt = datetime.now(timezone(timedelta(hours=0, minutes=0)))
format = input("What time format do you prefer (12hr or 24hr): ")
if format == "24hr":
    utc = dt.strftime("%H:%M:%S")
    t = now.strftime("%H:%M:%S")
    print("Local: " + t)
    print("UTC-0: " + utc)  
elif format == "12hr":
    t = datetime.strftime(now, "%I:%M:%S %p")
    utc = datetime.strftime(dt, "%I:%M:%S %p")
    print("Local: " + t)
    print("UTC-0: " + utc)
