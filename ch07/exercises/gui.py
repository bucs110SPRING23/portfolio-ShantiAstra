#I would like to add a disclaimer that I do not play super mario bros and do not know the specifics of how it is played
class Player:
  def __init__(self, pnum=1):
    """
    Initialize the player object
    Arguments: pnum is an int, the player's id number
    """
    self.player_num = pnum
    self.lives = 3 
    self.icon = "Mario" #default is Mario but maybe you can play as a different character
    self.big = False
    self.jump_height = 5

class MushroomEnemy:
    def __init__(self, hp = 2):
        """
        Initialize an enemy mushroom
        Arguments: hp is an int describing the amount of damage it must take to disappear
        """
        self.health = hp
        self.color = "red"
        self.bounce = 1 #height that the mushroom bounces while not stunned or dead
        self.deal_damage = 1 #number of lives lost when player gets hit
class MysteryBox:
    def __init__(self):
       """
       Initialize a mystery box block that can give rewards
       """
       self.height = 5
       self.distance = 70 #distance from beginning of level
       self.reward_box = ("Gold", "a flower", "poison", "Life Mushroom", "Super Mushroom") # the things the mystery box can give if successfully hit
