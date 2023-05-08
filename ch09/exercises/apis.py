import requests
import cv2
import sys
class Duck:
    def __init__(self, num = None):
        self.url = 'https://random-d.uk/api'
        if num == None:
            self.key = '/randomimg'
        else:
            self.key = f'/:{num}.jpg'
    def get(self):
        thisduck = requests.get(f'{self.url}?{self.key} format = json')
        display = cv2.imread(thisduck, cv2.IMREAD_ANYCOLOR)
        while True:
            cv2.imshow("Your Duck", display)
            cv2.waitkey()
            sys.exit()
        cv2.distroyAllWindows()

def main():
    if str(input("Do you want a random duck")) == "yes":
        duckID = None
    else:
        duckID = int(input("Please give an ID number for your duck"))
    newduck = Duck(duckID)
    newduck.get()

main()