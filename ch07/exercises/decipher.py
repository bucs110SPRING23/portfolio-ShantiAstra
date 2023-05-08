def convert(message):
    newmessage = ""
    encodes = {"T":"K", "h":"y",
                "e":"v", "q":"h",
                "u":"l", "i":"z",
                "c":"t", "k":"b",
                "b":"s", "r":"i",
                "o":"f", "w":"n",
                "n":"e", "f":"w",
                "x":"o", "j":"a",
                "m":"d", "p":"g",
                "ed":"j", "v":"m", 
                #Note there is an error here
                #the word "jumped" in the file I was given 
                #is only 5 letters long and must be spelled strangely, 
                #so I did this workaround
                "r":"i", "t":"k",
                "l":"c", "d":"u",
                "a":"r", "z":"q", 
                "y":"p", "g":"x",
                " ":" "}
    decodes = {value:key for key, value in encodes.items()}
    for i in message:
        newmessage = newmessage + decodes[i]
    return newmessage

def main():
    filename = input("Which file would you like to convert")
    openfile = open(filename)
    file = str(openfile.read())
    openfile.close()
    print(file)
    converted_message = str(convert(file))
    newfilename = input("Where would you like the encoded version saved?")
    newfile = open(newfilename + ".txt", "w")
    print(converted_message)
    newfile.write(converted_message)
    newfile.close()
main()