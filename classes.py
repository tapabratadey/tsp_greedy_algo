# Package class that holds a package's data
class Package:
    def __init__(self, id, address, city, state,
                zip, deadline, weight, notes):
        self.id = id,
        self.address = address,
        self.city = city,
        self.state = state,
        self.zip = zip,
        self.deadline = deadline,
        self.weight = weight,
        self.notes = notes

    # __str__ func to convert data obj to string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (
            self.id,
            self.address,
            self.city,
            self.state,
            self.zip,
            self.deadline,
            self.weight,
            self.notes)

# # Truck class to store truck info
# class Truck:
#   def __init__(self, name):
#     self.name = name,
#     # self.package_info = package_info
#     self.package_info = []

#   def load_package(self, package):
#       self.package_info.append(package)

#   def __str__(self):
#       return "%s, %s" % (self.name, self.package_info)