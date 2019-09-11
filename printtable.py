def multtable(number, limit):
    for i in range(1, limit+1):
        print(i * number)

multtable(7, 10)

import math

def powertable(number, limit):
    for i in range(1, limit+1):
        power = math.pow(i, number)
        i =+ 1
        print(power)
powertable(2,4)
powertable(3,3)
