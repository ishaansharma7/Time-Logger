from time_logger import time_logger     # import time_logger

import time


'''~~~~~~~~~~~~~~~~~~~~~~~~~Function Example~~~~~~~~~~~~~~~~~~~~~~~~~'''

@time_logger()      # no location given automatically create a location named generic-logs and store log file
def say_hi():       # name of log file will be say_hi
    time.sleep(2)
    print("Hi")

@time_logger(location='example-location')   # create a location named as example-location if not already present
def say_hello():                            # name of log file will be say_hello
    time.sleep(1)
    print("Hello")

say_hi()
say_hello()


'''~~~~~~~~~~~~~~~~~~~~~~~~~~Class Example~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @time_logger(location='Employee')   # create a location named as Employee if not already present
    def print_name(self):               # name of log file will be print_name
        time.sleep(1)
        print(self.name)
    
    @time_logger(location='Employee')   # create a location named as Employee if not already present
    def print_age(self):                # name of log file will be print_age
        time.sleep(3)
        print(self.age)

obj = Employee('Isaac', 21)
obj.print_name()
obj.print_age()
