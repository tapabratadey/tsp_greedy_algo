import package_handler as pckg_hndl

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
    if (package.deadline != 'EOD' or package.id == 19):
      if 'Delayed' not in package.notes:
          first_delivery.append(package)
          pckg_hndl.updt_first_del_sTime(package)

#9:05
def load_second_delivery(package):
    if 'Delayed' in package.notes or 'Can only ' in package.notes:
      second_delivery.append(package)
      pckg_hndl.updt_second_del_sTime(package)

def load_third_delivery(package):
    # packages in same address
    # and the wrong address listed
    if ('10:30' not in package.deadline
        and '84104' in package.zip):
          third_delivery.append(package)
          pckg_hndl.updt_third_del_sTime(package)
    if 'Wrong address listed' in package.notes:
        package.address = ('410 S State St')
        package.zip = '84111'
        third_delivery.append(package)
        pckg_hndl.updt_third_del_sTime(package)

def load_remaining_packages(package):
  # remaining    
  if (package not in first_delivery and
      package not in second_delivery and
      package not in third_delivery):
        if (package.zip == '84115' or
            package.address == '1330 2100 S'):
              first_delivery.append(package)
              pckg_hndl.updt_first_del_sTime(package)
        elif (package.zip == '84111' or
            package.zip == '84119' or
            package.zip == '84117'):
              second_delivery.append(package)
              pckg_hndl.updt_second_del_sTime(package)
        else:
          third_delivery.append(package)
          pckg_hndl.updt_third_del_sTime(package)
