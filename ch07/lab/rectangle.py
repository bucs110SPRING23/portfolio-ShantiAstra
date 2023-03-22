class Rectangle:
    def __init__(self, x,y,h, w):
        """
        Initialize a rectangle object.
        arguments: self is the object created, x and y are integers that serve as coordinates,
        and w and h are integers describing the size of the rectangle
        """
        self.x = abs(x)
        self.y = abs(y)
        self.width = abs(w)
        self.height = abs(h)
    def __str__(self):
        mystr = "This rectangle starts at " + str(self.x) +", " + str(self.y) + " and is " + str(self.width) + "long and " + str(self.height) + "tall." 
        return mystr
