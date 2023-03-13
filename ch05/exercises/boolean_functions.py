def percentage_to_letter(score= 0):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def is_passing(letter = None):
    if letter == "A" or letter == "B" or letter == "C":
        return True
    else:
        return False
score = int(input("What percent of points did you earn on the exam?"))
letter = percentage_to_letter(score)
if is_passing(letter):
    print("Congratulations! You passed the exam")    
else:
    print("Oh no, better get to studying! You have failed this exam")