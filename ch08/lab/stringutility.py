class StringUtility:
    def __init__(self, string):
        """
        initialize a string object
        Arguments: string is a str that becomes the object's first parameter
        """
        self.string = string
    def __str__(self):
        return self.string
    def vowels(self):
        for i in self.string:
            if i == i or I or a or A or e or E or o or O or u or U or y or Y