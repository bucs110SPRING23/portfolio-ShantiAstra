import rectangle
class Surface:
    def __init__(self, filename, x, y, h, w):
        """
        Initializes the surface object.
        Arguments: self is the surface object, filename is a string, 
        x, y, w, and h are the parameters that define the position and size of the rectangle
        """
        self.image = str(filename)
        self.rect = rectangle.Rectangle(x,y,h,w)
    def getRect(self):
        """
        returns the rectangle object that belongs to this surface
        Arguments: self is the surface object
        """
        return self.rect