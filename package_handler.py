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

def updt_pkg_loc(delivery_num, csv_address):
	for i in range(len(delivery_num)):
		for j in range(len(csv_address)):
			if (delivery_num[i].address == csv_address[j][2]):
				delivery_num[i].address_location = int(csv_address[j][0])
				print(delivery_num[i])

def fastest_route(delivery_list, delivery_num, current_loc, csv_address_data):
	if (len(delivery_list) == 0):
		return delivery_list
	else:
		min_dist = 40.0
		new_loc = 0
		for i in range(len(delivery_list)):
			curr_dist = find_current_dist_val(current_loc,
											delivery_list[i].address_location,
											csv_address_data)
			if curr_dist <= min_dist:
				min_dist = curr_dist
				new_loc = delivery_list[i].address_location
				# print(min_dist)

def find_current_dist_val(row, col, csv_address_data):
	curr_dist = csv_address_data[row][col]
	if curr_dist == '':
		curr_dist = csv_address_data[col][row]
	return float(curr_dist)