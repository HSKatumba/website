class vehicle(object):
    def __init__(self,number_of_wheels,type_of_tank,seating_capacity,maxi_velo):
        self.number_of_wheels=number_of_wheels
        self.type_of_tank=type_of_tank
        self.seating_capacity=seating_capacity
        self.maxi_velo=maxi_velo

        @property
        def number_of_wheels(self):
            return self._number_of_wheels

        @number_of_wheels.setter
        def number_of_wheels(self,number):
            self._number_of_wheels=number


car=vehicle(4,"electric",5,250)

print(car.number_of_wheels)
        
car.number_of_wheels = 10
print(car.number_of_wheels)
