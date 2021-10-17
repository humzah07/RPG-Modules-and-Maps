def introduction():
    """ Prints out the introduction
    of the game """
    print("""
  Batman and Green Lantern are on a mission to find an underground enemy base.
  While they are looking for the base, the enemy is notified of their mission
  Batman and Green Lantern need to find their way out and escape the temple.

  You can go only four directions to escape:
  forward, backward, right, left

  You also have an option to quit, 
  which is accessible in the menu
  
  Here is a printed map of the temple. You can use this or a hint,
  provided in the menu, to find your way out of the temple

  """)
    print(temple_map)

# This defines the layout of the temple
# Level 1 is where the user starts in the game
# Level 10 is where the game finishes
temple_map = [
     ["Blank", "Blank", "Blank", "Level 10" , "Blank"   ],
     ["Blank", "Blank", "Blank", "Level 9", "Blank"],
     ["Blank", "Blank", "Level 7", "Level 8", "Blank"],
     ["Blank", "Blank", "Level 6", "Blank", "Blank"],
     ["Blank", "Level 4", "Level 5", "Blank", "Blank"],
     ["Blank", "Level 3", "Blank", "Blank", "Blank"],
     ["Blank", "Level 2", "Level 1", "Blank", "Blank"],
 ]




