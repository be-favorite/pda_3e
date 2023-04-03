# Chapter 2 Dates and times
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day
dt.month
dt.year
dt.minute
type(dt)

type(dt.strftime("%Y-%m-%d %H:%M"))

type(datetime.strptime("20091031", "%Y%m%d"))
