def star_pyramid():
    stars_in_row = 1
    length = int(input("How tall would you like your star pyramid?"))
    for _ in range(length):
        print("*" * stars_in_row)
        stars_in_row +=1
def rstar_pyramid():
    length = int(input("How tall would you like your upside-down star pyramid?"))
    stars_in_row = length
    for _ in range(length):
        print("*" * stars_in_row)
        stars_in_row -=1

star_pyramid()
rstar_pyramid()