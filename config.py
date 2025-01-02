import configparser, os

config = configparser.ConfigParser()



def create_config():
    with open("config.ini", "w") as filepath:
        config.write(filepath)

def create_items_file():
    with open("items_schedule.ini", "w") as filepath:
        config.write(filepath)

def settings():
    name = "Settings"
    
    config.read("config.ini")

    if not config.has_section(name):
        config.add_section(name)

    if not os.path.exists("config.ini"):
        create_config()

    os.system("cls")
    print("Here are your settings:\n ")

    for section in config.sections():
        print(f"[{section}]")
        for key, value in config.items(section):
            print(f"{key} = {value}")
    
    print("\n")

    
    aura = str(input("Which aura you want to be auto equipped: "))

    webhook_url = str(input("Write your webhook url to get screenshots: "))

    userid = int(input("Whats your user id? (to get pinged): "))


    config.set("Settings", "AURATOEQUIP", aura)
    config.set("Settings", "WEBHOOKURL", webhook_url)
    config.set("Settings", "USERID", str(userid))

    with open("config.ini", "w") as finishconfig:
        config.write(finishconfig)


def save_to_ini(filepath, items_for_schedule):
    name = "Items"

    if not os.path.exists(filepath):
        create_items_file()
    
    config.read(filepath)

    if name not in config.sections():
        config.add_section(name)

    config["Items"] = {}
    for item, cooldown in items_for_schedule.items():
        config["Items"][item] = str(cooldown)
    
    with open(filepath, "w") as finishconfig:
        config.write(finishconfig)

    

def item_schedule():
    filepath = "items_schedule.ini"

    config.read("items_schedule.ini")

    print("Your items that are in schedule:\n")

    for section in config.sections():
        for item, cd in config.items(section=section):
            print(f"Name: {item.capitalize()} Cooldown: {cd.capitalize()} seconds")

    print("\n")

    try:
        items_amount = int(input("How many items you want to use?: "))
        if items_amount <= 0:
            print("What you want to use then?? The number of items must be greater than 0. ")
    except ValueError:
        print("Valid number")
        return

    items_dict = {}

    for i in range(items_amount):
        item_to_use = input(f"Enter name of item {i + 1}: ").strip()
        if not item_to_use:
            print("It cant be empty.")
            return
        
        try:
            cooldown = int(input(f"Write cooldown for {item_to_use} (in seconds): "))
            if cooldown <= 0:
                print("Cooldown supposed to be greater than 0.")
                return
        except ValueError:
            print("Wrong number for cooldown.")
            return
        
        items_dict[item_to_use] = cooldown

        save_to_ini(filepath=filepath, items_for_schedule=items_dict)

        print("\nItems has been saved.\n")


    



