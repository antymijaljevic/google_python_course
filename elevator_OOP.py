class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.current = current
        self.bottom = bottom
        self.top = top
        
    def __str__(self):
        return "Current floor: {}".format(self.current)
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current == self.top:
            pass
        else:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current == self.bottom:
            pass
        else:
            self.current -= 1
        
        pass
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        pass

elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.up()
print(elevator)

elevator.go_to(9)
print(elevator)

elevator.up()
elevator.up()
print(elevator)

elevator.go_to(1)
print(elevator)

elevator.down()
print(elevator)

elevator.down()
elevator.down()
elevator.down()
print(elevator)

elevator.go_to(5)
print(elevator)
