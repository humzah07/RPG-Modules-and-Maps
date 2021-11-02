inventory_input = input("Batman or Green Lantern: ")

# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """Use the Night Vision Goggles to see in the dark
                        and find your way""",
                         "damage": 0, "protection": 0},
                        },
             "Green Lantern": {"Power Ring":
                           {"description":
                            "Use this ring as a flashlight to find their way",
                            "damage": 0, "protection": 0}}
                    }


# This function defines the player inventory


def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    protection_items = []
    weapons = []
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        print(f"{player}'s {item} - {description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")
        if protection != 0 and damage == 0:
            protection_items.append(item)
        elif damage != 0:
            weapons.append(item)
    return protection_items, weapons

