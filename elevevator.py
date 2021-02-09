""" Simulates the an elevator """

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        pass

    def __str__(self):
        return "The elevator is in the {}th floor".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < 10:
            self.current += 1
        #print(self.current)
        pass

    def down(self):
        if self.current >-1:
            self.current -= 1
        #print(self.current)
        pass

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.current < 10 and self.current > -1 :
            self.current = floor
        #print(self.current)
        pass



"""instanciate the elevator class"""
elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.current #should output 1

elevator.go_to(10)
elevator.current #should output 10

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(str(elevator))





