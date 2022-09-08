class Circle:

    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def __contains__(self, point):
        if sum((a - b) ** 2 for a, b in zip(self.centre, point)) < self.radius ** 2:
            return True
        else:
            return False
