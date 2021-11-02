# Course: CS 30
# Period: 2
# Date created: 19/09/21
# Date last modified: 21/09/21
# Name: Humzah Zahid Malik
# Description: Batman x Green Lantern - Temple Escape


import actions
import Characters
import os
import sys
import intro
import class_functions


inventory_input = input("Batman or Green Lantern: ")

# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """Use the Night Vision Goggles to see
                        in the dark and find your way""" ,}},
             "Green Lantern": {"Power Ring":
                           {"description":
                            "Use this ring as a flashlight to find your way",}}
             }


def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        print(f"{player}'s {item} - {description}")

while True:
    if inventory_input == "Batman":
        Characters.character_intro()
        Characters.batman_class()
        Characters.Batman_inventory()
        class_functions.firstTiles()
        player_inventory("Batman", inventory)
        actions.action_1()
        actions.action_2()
        actions.action_3()
        actions.action_4()
        actions.action_5()
        actions.action_6()
        actions.action_7()
        actions.action_8()
        actions.action_9()
        actions.action_9()
        quit()
    if inventory_input == "Green Lantern":
        intro.introduction()
        Characters.character_intro_2()
        Characters.green_lantern_class()
        Characters.Green_lantern_inventory()
        player_inventory("Green Lantern", inventory)
        actions.actions_1()
        actions.actions_2()
        actions.actions_3()
        actions.actions_4()
        actions.actions_5()
        actions.actions_6()
        actions.actions_7()
        actions.actions_8()
        actions.actions_10()
        quit()
    else:
        print("invalid action")
        os.execl(sys.executable, sys.executable, *sys.argv)
