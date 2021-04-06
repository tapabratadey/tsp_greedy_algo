import datetime as dt
# import calc_dist as dist
import algo as algo

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

def updt_pkg_loc(delivery_list, csv_address):
	for i in range(len(delivery_list)):
		for j in range(len(csv_address)):
			if (delivery_list[i].address == csv_address[j][2]):
				delivery_list[i].address_location = int(csv_address[j][0])

def updt_starting_loc():
	algo.first_deliv_sorted_idx.insert(0, '0')
	algo.second_deliv_sorted_idx.insert(0, '0')
	algo.third_deliv_sorted_idx.insert(0, '0')