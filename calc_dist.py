import csv
import load_truck as truck
import package_handler as pckg_hndl

dist_data = []
dist_data_name = []

with open("csv/distance_table_data.csv") as dist_data_file:
	dist_data = list(csv.reader(dist_data_file, delimiter=','))

with open("csv/distance_table_data_name.csv") as dist_data_name_file:
	dist_data_name = list(csv.reader(dist_data_name_file, delimiter=','))

first_total_dist = 0
second_total_dist = 0
third_total_dist = 0

def updt_packages():
	pckg_hndl.updt_pkg_loc(truck.first_delivery, dist_data_name)
	pckg_hndl.updt_pkg_loc(truck.second_delivery, dist_data_name)
	pckg_hndl.updt_pkg_loc(truck.third_delivery, dist_data_name)

def find_fastest_route():
	pckg_hndl.fastest_route(truck.first_delivery, "first", 0, dist_data)

def total_dist():
	updt_packages()
	find_fastest_route()
	return first_total_dist + second_total_dist + third_total_dist
