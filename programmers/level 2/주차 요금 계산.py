from collections import defaultdict
import math 

def time_to_minute(time):
    tmp = list(map(int, time.split(':')))
    minute = 60 * tmp[0] + tmp[1]
    return minute


class Parking:
    def __init__(self, fees):
        self.basic_time, self.basic_charge, self.unit_time, self.unit_charge = fees
        self.parking = False
        self.in_time = 0
        self.total = 0

    def update(self, time, action):
        self.parking = True if action=='IN' else False
        if self.parking:  
            self.in_time = time_to_minute(time)
        else:
            self.total += (time_to_minute(time) - self.in_time)

    def calc_fee(self):
        if self.parking: 
            self.update('23:59', 'OUT')
        if self.total < self.basic_time:
            return self.basic_charge
        else:
            return self.basic_charge + math.ceil((self.total - self.basic_time) / self.unit_time) * self.unit_charge


def solution(fees, records):
    recordsDict = defaultdict(lambda:Parking(fees))
    for record in records:
        time, car, action = record.split()
        recordsDict[car].update(time, action)
    return [v.calc_fee() for k, v in sorted(recordsDict.items())]