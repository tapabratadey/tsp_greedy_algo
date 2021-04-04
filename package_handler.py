import load_truck as truck
import datetime as dt

# time conversion
(h, m, s) = "08:00:00".split(':')
first_del_sTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

(h, m, s) = "09:05:00".split(':')
second_del_sTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

(h, m, s) = "11:00:00".split(':')
third_del_sTime = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# updating start time of packages
def updt_first_del_sTime(package):
		package.start_time = first_del_sTime
def updt_second_del_sTime(package):
		package.start_time = second_del_sTime
def updt_third_del_sTime(package):
		package.start_time = third_del_sTime
