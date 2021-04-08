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

# updating package locations
# O(n^2)
def updt_pkg_loc(delivery_list, csv_address):
  for i in range(len(delivery_list)):
    for j in range(len(csv_address)):
      if (delivery_list[i].address == csv_address[j][2]):
        delivery_list[i].address_location = int(csv_address[j][0])

# updating sorted list for each delivery.
# setting the starting point to from location 0
def updt_starting_loc():
  algo.first_deliv_sorted_idx.insert(0, 0)
  algo.second_deliv_sorted_idx.insert(0, 0)
  algo.third_deliv_sorted_idx.insert(0, 0)

def updt_delivery(delivered_time, sorted_deliv, my_hash, deliv_num):
  sorted_deliv.status = delivered_time
  id = sorted_deliv.id
  my_hash.add(id, deliv_num)

def updt_del_time_n_hash(delivered_time, i, my_hash, truck):
  updt_delivery(delivered_time, algo.first_deliv_sorted[i],
                my_hash, truck.first_delivery)
  updt_delivery(delivered_time, algo.second_deliv_sorted[i],
                my_hash, truck.second_delivery)
  updt_delivery(delivered_time, algo.third_deliv_sorted[i],
                my_hash, truck.third_delivery)
  
def calc_pckg_time(get_curr_dist, deliv_time_list):
  pckg_time = get_curr_dist / 18
  conv_time_format = '{0:02.0f}:{1:02.0f}'.format(*divmod(pckg_time * 60, 60)) + ':00'
  deliv_time_list.append(conv_time_format)
  deliv_time = (dt.timedelta())
  for i in range(len(deliv_time_list)):
    (h, m, s) = deliv_time_list[i].split(':')
    conv = dt.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    deliv_time += conv
  return deliv_time