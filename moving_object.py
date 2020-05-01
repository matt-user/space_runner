"""Moving object class that defines the functionality for a moving object."""

import operator

from pygame.math import Vector2

from utility import get_direction

class MovingObjectMixin:

    def __init__(self, speed):
        """Moving object constructor"""
        self.speed = speed
        self.is_moving = False
        self.delta = (0, 0)

    def start_moving(self, destination):
        """Tells the moving object to start moving to the point."""
        if self.get_pos() == destination:
            if self.is_moving:
                self.stop_moving()
            return
        self.is_moving = True
        self.destination = destination
        self.compute_delta()

    def compute_delta(self):
        """Compute the change in the x and y direction for each update"""
        direction = self.destination - self.get_pos()
        # x_dir, y_dir = get_direction(self.get_pos(), self.destination)
        direction.normalize_ip()
        self.delta = (direction.x * self.speed, direction.y * self.speed)

    def update_location(self):
        """Update the location of the moving object."""
        # if the difference between the destination and the moving object 
        # is small enough, consider us at the destination.
        if self.is_at_location(self.destination):
            self.set_pos(self.destination)
            self.stop_moving()
            return True
        self.rect.move_ip(self.delta[0], self.delta[1])
        # x_dir, y_dir = get_direction(self.get_pos(), self.destination)
        # self.rect.move_ip(self.speed * x_dir, self.speed * y_dir)
        return False

    def is_at_location(self, point):
        """Returns whether the enemy is at the given point."""
        dif = self.destination - self.get_pos()
        print(f"dets: {self.destination} pos: {self.get_pos()}")
        print(f"dif: {dif} delta: {self.delta}")
        # x_dif, y_dif = map(operator.sub, point, self.get_pos())
        return (abs(dif.x) <= abs(self.delta[0])) and (abs(dif.y) <= abs(self.delta[1]))
    
    def set_pos(self, point):
        """Sets the position of the moving object"""
        self.gun_pos = point
        self.rect.center = self.gun_pos - ((self.original_surf.get_height() / 2) * self.direction)

    def stop_moving(self):
        """Tells this object to stop moving"""
        self.is_moving = False
        self.destination = None
