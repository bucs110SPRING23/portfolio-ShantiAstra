# Caesar Cipher by Shanti Astra
# converts alphanumeric characters. Converts everything into lowecase
def test_message():
    file = open("test", "w")
    file.write("The quick brown fox jumped over the lazy dog")
    file.close()
def convert(message):
    newmessage = ""
    keycodes = {"a":"f", "A":"F",
                "b":"y", "B":"Y",
                "c":"i", "C":"I",
                "d":"e", "D":"E",
                "e":"n", "E":"N",
                "f":"l", "F":"L",
                "g":"x", "G":"X",
                "h":"8", "H":"0",
                "i":"h", "I":"H",
                "j":"d", "J":"D", 
                "k":"p", "K":"P",
                "l":"3", "L":"4", 
                "m":"w", "M":"W",
                "n":"2", "N":"6",
                "o":"s", "O":"S",
                "p":"a", "P":"A",
                "q":"g", "Q":"G",
                "r":"t", "R":"T",
                "s":"5", "S":"7",
                "t":"b", "T":"B",
                "u":"o", "U":"O",
                "v":"k", "V":"K",
                "w":"r", "W":"R",
                "x":"7", "X":"7",
                "y":"z", "Y":"Z",
                "z":"c", "Z":"C",
                "1":"9", "2":"j",
                "3":"m", "4":"q",
                "5":"r", "6":"u",
                "7":"d", "8":"v",
                "9":"1", "0":"j",
                " ":" "}
    for i in message:
        newmessage = newmessage + keycodes[i]
    return newmessage

def main():
    filename = input("Which file would you like to convert")
    openfile = open(filename)
    file = str(openfile.read())
    openfile.close()
    print(file)
    converted_message = str(convert(file))
    newfilename = input("Where would you like the encoded version saved?")
    newfile = open(newfilename, "w")
    print(converted_message)
    newfile.write(converted_message)
    newfile.close()
test_message()
main()