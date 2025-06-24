# class Point():
#     def __init__(self,x,y):
#         self.x :int =  int(input("Enter x coordinate: "))
#         self.y :int = int(input("Enter y coordinate: "))



# p = Point(0, 0)  # The parameters are not used in this case, as input is taken in the constructor
# print(f"Point coordinates: ({p.x}, {p.y})")



class Flight():

    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    # Method to add a passenger to the flight
    # If the flight is full, it will not add the passenger
    # and will print a message indicating that the flight is full.
    # If the flight is not full, it will add the passenger
    def add_passenger(self,name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            return f"Passenger {name} added. Current passengers: {self.passengers}"
        else:
            return f"Flight is full. Cannot add {name} passenger."

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
peoples = ['Alice', 'Bob', 'Charlie', 'David']
for people in peoples:
    print(flight.add_passenger(people))  # Try to add each passenger
print(flight.open_seats())  # Should print the number of open seats left

