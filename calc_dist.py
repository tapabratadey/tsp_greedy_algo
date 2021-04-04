import csv

def read_distance_data(filename, tag):
	if tag == "data":
		with open(filename) as dist_data_file:
			dist_data = list(csv.reader(dist_data_file, delimiter=','))
			# print(dist_data[1][0])
	if tag == "name":
		with open(filename) as dist_data_name_file:
			dist_data_name = list(csv.reader(dist_data_name_file, delimiter=','))
			# print(dist_data_name[1][0])


# def d


# sort the truck packages
# 
		

