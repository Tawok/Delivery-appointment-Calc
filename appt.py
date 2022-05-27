import datetime
import math


class appointment:
    def __init__(self, load_date, arrival_date, distance, speed, window_time):
        self.load_date = load_date
        self.arrival_date = arrival_date
        self.distance = distance
        self.speed = speed
        self.window_time = window_time

    def cal_dates(self):
        depature = datetime.datetime.strptime(
            ','.join(self.load_date.split('/')), '%m,%d,%Y')
        arrival = datetime.datetime.strptime(
            ','.join(self.arrival_date.split('/')), '%m,%d,%Y')
        return depature - arrival

    def driving_time(self):
        result = self.distance/(self.speed*11)
        driving_days = datetime.timedelta(days=math.floor(result))
        driving_hours = datetime.timedelta(
            hours=math.ceil(math.modf(result)[0]*11))
        return driving_days + driving_hours

    def total_delivery(self):
        return self.driving_time() + datetime.timedelta(hours=self.window_time)

    def reciever_appointment(self, location1, location2):
        location1 = location1.lower()
        location2 = location2.lower()
        if location1 == 'et':
            if location2 == 'et':
                return self.total_delivery() - datetime.timedelta(hours=0)
            if location2 == 'ct':
                return self.total_delivery() - datetime.timedelta(hours=1)
            if location2 == 'mt':
                return self.total_delivery() - datetime.timedelta(hours=2)
            if location2 == 'pt':
                return self.total_delivery() - datetime.timedelta(hours=3)
        if location1 == 'ct':
            if location2 == 'et':
                return self.total_delivery() + datetime.timedelta(hours=1)
            if location2 == 'ct':
                return self.total_delivery() - datetime.timedelta(hours=0)
            if location2 == 'mt':
                return self.total_delivery() - datetime.timedelta(hours=1)
            if location2 == 'pt':
                return self.total_delivery() - datetime.timedelta(hours=2)
        if location1 == 'mt':
            if location2 == 'et':
                return self.total_delivery() + datetime.timedelta(hours=2)
            if location2 == 'ct':
                return self.total_delivery() + datetime.timedelta(hours=1)
            if location2 == 'mt':
                return self.total_delivery() - datetime.timedelta(hours=0)
            if location2 == 'pt':
                return self.total_delivery() - datetime.timedelta(hours=1)
        if location1 == 'pt':
            if location2 == 'et':
                return self.total_delivery() + datetime.timedelta(hours=3)
            if location2 == 'ct':
                return self.total_delivery() + datetime.timedelta(hours=2)
            if location2 == 'mt':
                return self.total_delivery() + datetime.timedelta(hours=1)
            if location2 == 'pt':
                return self.total_delivery() - datetime.timedelta(hours=0)


transit = appointment('08/16/2021', '08/20/2021', 2321, 50, 2)

print(f"driving time: {transit.driving_time()}")
print(f"delivery time: {transit.total_delivery()}")  # 2h window
# +2h east
print(f"hour diference: {transit.reciever_appointment('MT', 'ET')}")
