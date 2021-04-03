first_delivery = []
second_delivery = []
third_delivery = []

# loading packages to three different trucks
# based on assumptions
def load_trucks(package):
    load_first_delivery(package)
    load_second_delivery(package)    
    load_third_delivery(package)
    load_remaining_packages(package)
    
#8:00
def load_first_delivery(package):
    if (package.deadline[0] != 'EOD' or package.id[0] == 19):
      if 'Delayed' not in package.notes:
          first_delivery.append(package)
          # print("first", package.id[0], package.zip[0], package.address[0])

#9:05
def load_second_delivery(package):
    if 'Delayed' in package.notes or 'Can only ' in package.notes:
      second_delivery.append(package)
      # print("second", package.zip[0], package.address[0])

def load_third_delivery(package):
    # packages in same address
    # and the wrong address listed
    if ('10:30' not in package.deadline[0]
        and '84104' in package.zip[0]):
          third_delivery.append(package)
    if 'Wrong address listed' in package.notes:
        package.address = '410 S State St'
        package.zip = '84111'
        third_delivery.append(package)

def load_remaining_packages(package):
  # remaining    
  if (package not in first_delivery and
      package not in second_delivery and
      package not in third_delivery):
        # print(package.id, package.address[0], package.zip[0])
        if (package.zip[0] == '84115' or
            package.address[0] == '1330 2100 S'):
              first_delivery.append(package)
        elif (package.zip[0] == '84111' or
            package.zip[0] == '84119' or
            package.zip[0] == '84117'):
              second_delivery.append(package)
        else:
          third_delivery.append(package)