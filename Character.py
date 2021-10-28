class Character(object):
    def __init__(self, name, birthplace, special_power):
        self.name = name
        self.special_power = special_power
        self.birthplace = birthplace

    def introduction(self):
      print(' Hi, my name is ', self.name) 

    def power(self):
      print("My special power is my", self.special_power)

    def birthplace(self):
      print("My birthplace is", self.birthplace)

def character_intro():
    """ Prints out the introduction for Batman """
    print("""
  You have chosen Batman as you character.
  You will use Batman to get out of this maze.
  You can use a hint to complete a level.
  """)
    batman = Character("Batman", "High Intelligence", "Gotham City")
    batman.introduction()
    batman.power()
    batman.birthplace()

# This function defines the intro for Green Lantern


def character_intro_2():
    """ Prints out the introduction for Green Lantern """
    print("""
     You have chosen Green Lantern as you character. 1
     You will use Green Lantern to get out of this maze.
     You can use a hint to complete a level.
    """)
