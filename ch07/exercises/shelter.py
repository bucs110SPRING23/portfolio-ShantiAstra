import time
class Adoptee:
    def __init__(self, name, type = "dog"):
        """
        Initialize an adoptable pet object
        arguments: a str for a name, and a str for species common name
        """
        self.name = name
        self.species = type
        self.id = id(self)
        self.arrival = time.strftime("%d/%m/%Y")
        self.available = True
        self.adoption = False
    def adopt(self, date = time.strftime("%d/%m/%Y")):
        """
        Adopt a pet. This changes the pet's availablility to false and adds a adoption date
        arguments: date is a string describing adoption date. Default is the date the program is run
        """
        self.available = False
        self.adoption = date
    def is_available(self):
        """
        Check if an animal is adoptable
        """
        if self.available:
            return self.name + " is available for adoption"
        else:
            return self.name + " has been adopted"
    
def main():
    rex = Adoptee("Rex", "pterodactyl")
    if str(input("Would you like to adopt Rex?")) == "yes":
        rex.adopt()
    print(rex.is_available())
main()