import datetime as dt
# import calc_dist as dist

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

first_delivery_list = []
second_delivery_list = []
third_delivery_list = []

def updt_first_pkg_loc(first_delivery, csv_address):
	for i in range(len(first_delivery)):
		for j in range(len(csv_address)):
			if (first_delivery[i].address == csv_address[j][2]):
				first_delivery_list.append(csv_address[j][0])
				first_delivery[i].address_location = csv_address[j][0]
				# print(first_delivery[i])

def updt_second_pkg_loc(second_delivery, csv_address):
	for i in range(len(second_delivery)):
		for j in range(len(csv_address)):
			if (second_delivery[i].address == csv_address[j][2]):
				second_delivery_list.append(csv_address[j][0])
				second_delivery[i].address_location = csv_address[j][0]
				# print(second_delivery[i])

def updt_third_pkg_loc(third_delivery, csv_address):
	for i in range(len(third_delivery)):
		for j in range(len(csv_address)):
			if (third_delivery[i].address == csv_address[j][2]):
				third_delivery_list.append(csv_address[j][0])
				third_delivery[i].address_location = csv_address[j][0]
				# print(third_delivery[i])
		