first_delivery_list = []
second_delivery_list = []
third_delivery_list = []

first_deliv_sorted = []
first_deliv_sorted_idx = []

second_deliv_sorted = []
second_deliv_sorted_idx = []

third_deliv_sorted = []
third_deliv_sorted_idx = []

def fastest_route(delivery_list, delivery_num, current_loc, csv_address_data):
	if (len(delivery_list) == 0):
		return delivery_list
	else:
		try:			
			min_dist = 40.0
			new_loc = 0
			curr_dist = 0
			find_min_dist(delivery_list,
										delivery_num,
										current_loc,
										csv_address_data,
										min_dist,
										new_loc,
										curr_dist)
		except IndexError:
			pass

def find_min_dist(delivery_list,
									delivery_num,
									current_loc,
									csv_address_data,
									min_dist,
									new_loc,
									curr_dist):
		for i in range(len(delivery_list)):
			temp = find_current_dist_val(current_loc,
											delivery_list[i].address_location,
											csv_address_data)
			if temp <= min_dist:
				min_dist = temp
				new_loc = delivery_list[i].address_location
		for i in range(len(delivery_list)):
			temp = find_current_dist_val(current_loc,
											delivery_list[i].address_location,
											csv_address_data)
			if (temp == min_dist):
				if (delivery_num == "first"):
					sort_first_delivery(delivery_list, i, current_loc, new_loc, csv_address_data)
				elif (delivery_num == "second"):
					sort_second_delivery(delivery_list, i, current_loc, new_loc, csv_address_data)
				elif (delivery_num == "third"):															
					sort_third_delivery(delivery_list, i, current_loc, new_loc, csv_address_data)

def sort_first_delivery(delivery_list, i, current_loc, new_loc, csv_address_data):
			first_deliv_sorted.append(delivery_list[i])
			first_deliv_sorted_idx.append(delivery_list[i].address_location)
			delivery_list.pop(delivery_list.index(delivery_list[i]))
			current_loc = new_loc
			fastest_route(delivery_list, "first", current_loc, csv_address_data)

def sort_second_delivery(delivery_list, i, current_loc, new_loc, csv_address_data):
			second_deliv_sorted.append(delivery_list[i])
			second_deliv_sorted_idx.append(delivery_list[i].address_location)
			delivery_list.pop(delivery_list.index(delivery_list[i]))
			current_loc = new_loc
			fastest_route(delivery_list, "second", current_loc, csv_address_data)

def sort_third_delivery(delivery_list, i, current_loc, new_loc, csv_address_data):
			third_deliv_sorted.append(delivery_list[i])
			third_deliv_sorted_idx.append(delivery_list[i].address_location)
			delivery_list.pop(delivery_list.index(delivery_list[i]))
			current_loc = new_loc
			fastest_route(delivery_list, "third", current_loc, csv_address_data)


def find_current_dist_val(row, col, csv_address_data):
	curr_dist = csv_address_data[row][col]
	if curr_dist == '':
		curr_dist = csv_address_data[col][row]
	return float(curr_dist)