import turtle
class lsystems:
    def __init__(self, axiom = "FX", iterations = 1, angle = 90, distance = 10, xpos = 0, ypos = 0):
        """
        Initialize a lsystems object.
        Arguments: 
            self is the object instance
            axiom is a string containing instructions
            iterations is an int that determines how many times the axiom is expanded
            angle is an int that determines the degree the turtle turns when told to
            distance is an int that determines the forward length of the lines the turtle draws
            xpos and ypos are ints that determine starting position
        """
        self.iterations = iterations
        self.distance = distance
        self.angle = angle
        self.axiom = axiom
        self.xpos = xpos
        self.ypos = ypos

    def generateInstructions(self):
        """
        Expands the axiom according to specific instructions for a defined number of loops
        """
        for _ in range(self.iterations):
            newstr = ""
            newbit = ""
            for i in self.axiom:
                if i == "X":
                    newbit = "X+YF"
                elif i == "Y":
                    newbit = "FX-Y"
                newstr += newbit
            self.axiom = newstr
    def visualize(self):
        """
        Draws a thing that represents the L-system based on the axiom
        """
        window = turtle.Screen()
        ellsey = turtle.Turtle()
        turtle.goto(self.xpos, self.ypos)
        for i in self.axiom:
            if i == "F":
                ellsey.forward(self.distance)
            elif i == "+":
                ellsey.right(self.angle)
            elif i == "-":
                ellsey.left(self.angle)
        window.exitonclick()

def main():
    myaxiom = str(input("What axiom should this L-system illustrate?"))
    myiter = int(input("How many times should this L-system repeat the rules generation?"))
    myangle = int(input("How many degrees should each turn be?"))
    mydistance = int(input("How far should each step go?"))
    mylsystem = lsystems(myaxiom, myiter, myangle, mydistance)
    mylsystem.generateInstructions()
    mylsystem.visualize()
   

main()