# vars to store sorted delivery trucks

first_deliv_sorted = []
first_deliv_sorted_idx = []

second_deliv_sorted = []
second_deliv_sorted_idx = []

third_deliv_sorted = []
third_deliv_sorted_idx = []

# gets called in calc_dist module
# calls find_min_dist to find mininum travel distance for a delivery truck
def fastest_route(delivery_list, delivery_num, current_loc, csv_address_data):
  if (len(delivery_list) == 0):
    return delivery_list
  else:
    try:
      min_dist = 20.0
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

# greedy algorithm O(n^2)

# first loop gets back the distance between two packages
# and compares with the min_dist which is initally set to 20
# and that address location is then stored in new_loc
# second loop again loops through deliver_list
# and calls sort_delivery() to add the new package info to
# a sorted list and stores its index, and pops the minimum
# distance from the original deliver_list
# updates the current location
# and calls the parent func fastest_route again recurssively


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
          sort_delivery(delivery_list, i, current_loc, new_loc, csv_address_data,
                        first_deliv_sorted, first_deliv_sorted_idx, "first")
        elif (delivery_num == "second"):
          sort_delivery(delivery_list, i, current_loc, new_loc, csv_address_data,
                        second_deliv_sorted, second_deliv_sorted_idx, "second")
        elif (delivery_num == "third"):															
          sort_delivery(delivery_list, i, current_loc, new_loc, csv_address_data,
                        third_deliv_sorted, third_deliv_sorted_idx, "third")

def sort_delivery(delivery_list, i, current_loc, new_loc, csv_address_data,
                        sorted_list, sorted_list_idx, msg):
      sorted_list.append(delivery_list[i])
      sorted_list_idx.append(delivery_list[i].address_location)
      delivery_list.pop(delivery_list.index(delivery_list[i]))
      current_loc = new_loc
      fastest_route(delivery_list, msg, current_loc, csv_address_data)

# finds distance value by getting data from csv_address_data
def find_current_dist_val(row, col, csv_address_data):
  curr_dist = csv_address_data[row][col]
  if curr_dist == '':
    curr_dist = csv_address_data[col][row]
  return float(curr_dist)