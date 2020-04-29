"""Moving object class that defines the functionality for a moving object."""

import operator

from utility import get_direction

class Moving_Object():

    def __init__(self, speed, rect):
        """Moving object constructor"""
        self.speed = speed
        self.is_moving = False
        self.delta = (0, 0)
        self.rect = rect

    def start_moving(self, point):
        """Tells the moving object to start moving to the point."""
        if self.get_pos() == point:
            if self.is_moving:
                self.stop_moving()
            return
        self.is_moving = True
        self.destination = point
        self.compute_delta()

    def compute_delta(self):
        """Compute the change in the x and y direction for each update"""
        x_dir, y_dir = get_direction(self.get_pos(), self.destination)
        self.delta = (x_dir * self.speed, y_dir * self.speed)

    def update_location(self):
        """Update the location of the moving object."""
        # if the difference between the destination and the moving object 
        # is small enough, consider us at the destination.
        if self.is_at_location(self.destination):
            self.set_pos(self.destination)
            self.stop_moving()
            return True
        x_dir, y_dir = get_direction(self.get_pos(), self.destination)
        self.rect.move_ip(self.speed * x_dir, self.speed * y_dir)
        return False

    def is_at_location(self, point):
        """Returns whether the enemy is at the given point."""
        x_dif, y_dif = map(operator.sub, point, self.get_pos())
        return (abs(x_dif) <= abs(self.delta[0])) and (abs(y_dif) <= abs(self.delta[1]))

    def get_pos(self):
        """Returns the middle front of an enemy"""
        x, y = self.rect.midtop
        return x, y
    
    def set_pos(self, point):
        """Sets the position of the moving object"""
        self.rect.midtop = point

    def stop_moving(self):
        """Tells this object to stop moving"""
        self.is_moving = False
        self.destination = None
