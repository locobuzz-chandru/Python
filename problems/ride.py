import random


class Driver:
    def __init__(self, driver_id, name, rating=0):
        self.driver_id = driver_id
        self.name = name
        self.rating = rating


class Passenger:
    def __init__(self, passenger_id, name, total_rides=0):
        self.passenger_id = passenger_id
        self.name = name
        self.total_rides = total_rides


class Ride:
    def __init__(self, ride_id, passenger_id, driver_id, destination, completed=False):
        self.ride_id = ride_id
        self.passenger_id = passenger_id
        self.driver_id = driver_id
        self.destination = destination
        self.completed = completed


class RideShare:
    def __init__(self):
        self.drivers = {}
        self.passengers = {}
        self.rides = {}

    def add_driver(self, driver):
        self.drivers[driver.driver_id] = driver
        return f"Driver '{driver.name}' is added"

    def add_passenger(self, passenger):
        self.passengers[passenger.passenger_id] = passenger
        return f"Passenger '{passenger.name}' is added"

    def get_available_driver_id(self):
        try:
            unavailable_drivers = [ride.driver_id for ride in self.rides.values() if not ride.completed]
            available_drivers = [driver for driver in self.drivers.keys() if driver not in unavailable_drivers]
            return available_drivers.pop(random.randint(0, len(available_drivers) - 1))
        except:
            raise Exception("all drivers are busy")

    def request_ride(self, passenger_id, destination):
        ride_id = len(self.rides) + 1
        driver_id = self.get_available_driver_id()
        self.rides[ride_id] = Ride(ride_id=ride_id, passenger_id=passenger_id, driver_id=driver_id,
                                   destination=destination)
        return f"Ride requested successfully\n" \
               f"Ride details-> Driver Name: {self.drivers[driver_id].name}, Passenger Name: {self.passengers[passenger_id].name}, Destination: {destination}"

    def rating(self, driver_id, rating):
        prev_rating = self.drivers[driver_id].rating
        new_rating = (prev_rating + rating) / (
            1 if len([ride.driver_id for ride in self.rides.values() if ride.driver_id == driver_id]) == 1 else 2)
        self.drivers[driver_id].rating = new_rating

    def complete_ride(self, ride_id, rating):
        try:
            self.rides[ride_id].completed = True
            self.passengers[self.rides[ride_id].passenger_id].total_rides += 1
            driver_id = self.rides[ride_id].driver_id
            self.rating(driver_id, rating)
            return f"Ride ID '{ride_id}' is completed"
        except:
            raise Exception("ride id does not exist")

    def get_total_drivers(self):
        return f"Total drivers: {len(self.drivers)}"

    def get_total_passengers(self):
        return f"Total passengers: {len(self.passengers)}"

    def get_active_rides(self):
        return f"Total active rides: {len([ride.ride_id for ride in self.rides.values() if not ride.completed])}"

    def get_completed_rides(self):
        return f"Total completed rides: {len([ride.ride_id for ride in self.rides.values() if ride.completed])}"

    def get_driver_with_highest_rating(self):
        ratings = {driver.rating: driver.name for driver in self.drivers.values()}
        return f"Driver with the highest rating: {ratings[max(ratings)]}"

    def get_passenger_with_most_rides(self):
        passengers = {passenger.total_rides: passenger.name for passenger in self.passengers.values()}
        return f"Passenger with most rides: {passengers[max(passengers)]}"


if __name__ == '__main__':
    ride_share = RideShare()
    A = Driver(driver_id=1, name="A")
    B = Driver(driver_id=2, name="B")
    C = Driver(driver_id=3, name="C")
    D = Driver(driver_id=4, name="D")
    E = Driver(driver_id=5, name="E")
    F = Driver(driver_id=6, name="F")
    G = Driver(driver_id=7, name="G")
    H = Driver(driver_id=8, name="H")
    I = Driver(driver_id=9, name="I")
    J = Driver(driver_id=10, name="J")

    for i in [A, B, C, D, E, F, G, H, I, J]:
        print(ride_share.add_driver(i))

    a = Passenger(passenger_id=1, name="a")
    b = Passenger(passenger_id=2, name="b")
    c = Passenger(passenger_id=3, name="b")
    d = Passenger(passenger_id=4, name="b")
    e = Passenger(passenger_id=5, name="b")
    f = Passenger(passenger_id=6, name="b")

    for i in [a, b, c, d, e, f]:
        print(ride_share.add_passenger(i))

    print(ride_share.request_ride(passenger_id=1, destination="Bangalore"))
    print(ride_share.request_ride(passenger_id=2, destination="Mumbai"))
    print(ride_share.complete_ride(ride_id=1, rating=4.2))
    print(ride_share.request_ride(passenger_id=1, destination="Mysore"))
    print(ride_share.request_ride(passenger_id=3, destination="Delhi"))
    print(ride_share.request_ride(passenger_id=4, destination="Hubli"))
    print(ride_share.complete_ride(ride_id=3, rating=4.1))
    print(ride_share.complete_ride(ride_id=2, rating=3.9))
    print(ride_share.request_ride(passenger_id=5, destination="Belgaum"))
    print(ride_share.request_ride(passenger_id=1, destination="Bangalore"))

    print(ride_share.get_total_drivers())
    print(ride_share.get_total_passengers())

    print(ride_share.get_active_rides())
    print(ride_share.get_completed_rides())

    print(ride_share.get_driver_with_highest_rating())
    print(ride_share.get_passenger_with_most_rides())
