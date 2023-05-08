class StringUtility:
    def __init__(self, string = ""):
        """
        initialize a string object
        Arguments: string is a str that becomes the object's first parameter
        """
        self.string = str(string)
    def __str__(self):
        """
        return the string that was used to define the object
        """
        return self.string
    def vowels(self):
        """
        count up all instances of vowels and return exact numbers up to 4 or "many"
        """
        return str(count) if (count := sum(self.string.count(i) for i in {"a","A","e","E","i","I","o","O","u","U","y","Y"})) < 5 else "many"
    def bothEnds(self):
        """
        return the first and last two characters in the string
        """
        return "" if len(self.string)<3 else self.string[0]+self.string[1] + self.string[-2] + self.string[-1]
    def fixStart(self):
        """
        replace all subsequent instances of the first character with asterisks
        """
        return self.string[0]+ "".join([i if i != self.string[0] else "*" for i in self.string[1:]]) if len(self.string) > 1 else self.string
    def asciiSum(self):
        """
        find the sum of the ASCII numbers that make up each character in the string
        """
        return sum([ord(i) for i in self.string])
    def cipher(self):
        """
        for each character, shift it forwards in the alphabet by a number equal to the length of the string. 
        Uppercase and lowercase ends of the alphabet wrap to the beginning of the alphabet in the same case
        """
        # non-looping characters are returned as-is instead of ciphered, while looped characters turn weird
        #return "".join([chr((ord(i)+len(self.string)) - (26* len(self.string)//26)) if ((len(self.string)%26 + ord(i)- (96 if i.islower() else 64) < 27) and (i.isalpha())) else (chr((ord(i)+len(self.string))-(26*((len(self.string)//26)+1))) if i.isalpha() else i) for i in self.string])
        
        # !!! This one works and seems to be doing the same thing as the second line above????
        
        list_of_chars = []
        for i in self.string:
            if i.isalpha():
                neword = ord(i) + len(self.string)
                if len(self.string)%26 + ord(i)- (96 if i.islower() else 64) < 27:
                    loops = len(self.string)//26
                else:
                    loops = len(self.string)//26 +1
                newchar= chr(neword - 26 * loops)
                list_of_chars.append(newchar)
            else:
                list_of_chars.append(i)
        result = "".join(list_of_chars)
        return result 

            
