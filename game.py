# Course: CS 30
# Period: 2
# Date created: 19/09/21
# Date last modified: 21/09/21
# Name: Humzah Zahid Malik
# Description: Batman x Green Lantern - Temple Escape


import action
import Character
import os
import sys
import intro


inventory_input = input("Batman or Green Lantern: ")

# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """Use the Night Vision Goggles to see
                        in the dark and find your way""" ,}},
             "Green Lantern": {"Power Ring":
                           {"description":
                            "Use this ring as a flashlight to find your way",}}
             }

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

def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        print(f"{player}'s {item} - {description}")

while True:
    intro.introduction()
    if inventory_input == "Batman":
        Character.character_intro()
        Character.batman_class()
        Character.Batman_inventory()
        player_inventory("Batman", inventory)
        action.action_1()
        action.action_2()
        action.action_3()
        action.action_4()
        action.action_5()
        action.action_6()
        action.action_7()
        action.action_8()
        action.action_9()
        action.action_9()
        quit()
    if inventory_input == "Green Lantern":
        intro.introduction()
        Character.character_intro_2()
        Character.green_lantern_class()
        Character.Green_lantern_inventory()
        player_inventory("Green Lantern", inventory)
        action.actions_1()
        action.actions_2()
        action.actions_3()
        action.actions_4()
        action.actions_5()
        action.actions_6()
        action.actions_7()
        action.actions_8()
        action.actions_10()
        quit()
    else:
        print("invalid action")
        os.execl(sys.executable, sys.executable, *sys.argv)
