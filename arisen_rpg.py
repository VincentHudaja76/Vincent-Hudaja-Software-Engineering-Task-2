#Arisen RPG - Vincent Hudaja

import customtkinter as ctk

arisen_rpg = ctk.CTk() #Initialise customtkinter as arisen_rpg
arisen_rpg.geometry("400x500") #Set window size
arisen_rpg.title("Arisen RPG") #Set window title
ctk.set_appearance_mode("dark") #Set window appearance to dark mode
ctk.set_default_color_theme("blue") #Set window default colour theme to blue

"""Other Variables"""
global character_selected
character_selected = ""
battle1_win = False
battle2_win = False
battle3_win = False

"""Character Classes"""
class Character:
    def __init__(self, name, health, damage, damage_buff, defence_buff, attack_buff_cost, defence_buff_cost):
        self.name = name
        self.health = health
        self.damage = damage
        self.damage_buff = damage_buff
        self.defence_buff = defence_buff
        self.attack_buff_cost = attack_buff_cost
        self.defence_buff_cost = defence_buff_cost
    def apply_damage_buff(self): #Apply damage buff method
        self.damage = self.damage + self.damage_buff #Add values to apply damage buff
        return self.damage #Return value
    def apply_defence_buff(self): #Apply health buff method
        self.health = self.health + self.defence_buff #Add values to apply health buff
        return self.health #Return value
    def show_stats(self): #Show stats method to display stats
        return self.name, self.health, self.damage, self.damage_buff, self.defence_buff #Return values
    def is_alive(self): #While loop method to determine if character is alive
        while self.health > 0: #Loop for if character health is above 0
            return True #Return alive as True if health is above 0
        else:
            return False #Return alive as False if health is not above 0
    def test_alive(self): #Test alive method for unit testing
        self.health = 0 #Sets health value to 0 for testing

class Fenix(Character):
    def __init__(self, name, health, damage, attack_buff, defence_buff, attack_buff_cost, defence_buff_cost):
        Character.__init__(self, name, health, damage, attack_buff, defence_buff, attack_buff_cost, defence_buff_cost)

class Flame(Character):
    def __init__(self, name, health, damage, attack_buff, defence_buff, attack_buff_cost, defence_buff_cost):
        Character.__init__(self, name, health, damage, attack_buff, defence_buff, attack_buff_cost, defence_buff_cost)

class Flow(Character):
    def __init__(self, name, health, damage, attack_buff, defence_buff, attack_buff_cost, defence_buff_cost):
        Character.__init__(self, name, health, damage, attack_buff, defence_buff, attack_buff_cost, defence_buff_cost)

fenix = Fenix("Fenix", 100, 20, 30, 20, 20, 20)
flame = Flame("Flame", 50, 50, 40, 10, 20, 20)
flow = Flow("Flow", 150, 10, 20, 50, 20, 20)

class Boss:
    def __init__(self, name, health, damage, damage_buff, defence_buff):
        self.name = name
        self.health = health
        self.damage = damage
        self.damage_buff = damage_buff
        self.defence_buff = defence_buff
    def apply_damage_buff(self): #Apply damage buff method
        self.damage = self.damage + self.damage_buff #Add values to apply damage buff
        return self.damage #Return value
    def apply_defence_buff(self): #Apply health buff method
        self.health = self.health + self.defence_buff #Add values to apply health buff
        return self.health #Return value
    def show_stats(self): #Show stats method to display stats
        return self.name, self.health, self.damage, self.damage_buff, self.defence_buff #Return values
    def is_alive(self): #While loop method to determine if boss is alive
        while self.health > 0: #Loop for if character health is above 0
            return True #Return alive as True if health is above 0
        else:
            return False #Return alive as False if health is not above 0
    def test_alive(self): #Test alive method for unit testing
        self.health = 0 #Sets health value to 0 for testing

"""Enemy Classes"""
class Enemy:
    def __init__(self, name, health, damage, special_buff):
        self.name = name
        self.health = health
        self.damage = damage
        self.special_buff = special_buff
    def apply_special(self):
        self.damage = self.damage + self.special_buff
        return self.damage
    def show_stats(self):
        return self.name, self.health, self.damage, self.special_buff
    def is_alive(self):
        while self.health > 0:
            return True
        else:
            return False
    def test_alive(self):
        self.health = 0

class Spooglin(Enemy):
    def __init__(self, name, health, damage, special_buff):
        super().__init__(name, health, damage, special_buff)

class Hopkin(Enemy):
    def __init__(self, name, health, damage, special_buff):
        super.__init__(self, name, health, damage, special_buff)

class Striker(Enemy):
    def __init__(self, name, health, damage, special_buff):
        super.__init__(self, name, health, damage, special_buff)

"""Other Classes"""
class Shop:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

item1 = Shop("Damage Potion", 20)
item2 = Shop("Health Potion", 20)

class Inventory:
    def __init__(self, item_name, amount):
        self.item_name = item_name
        self.amount = amount
    def add_item(self): #When battles are won or items are purchased, add item method is called
        self.amount = self.amount + 1
        return self.amount
    def remove_item(self): #When items are used, remove item method is called
        self.amount = self.amount - 1
        return self.amount
    def show_items(self):
        return self.item_name, self.amount

coins = Inventory("Coins", 20)
damage_potions = Inventory("Damage Potions", 0)
health_potions = Inventory("Health Potions", 0)

"""Game Functions/Processes"""
def hide_frames(): #Function to remove frames
    menu_frame.place_forget()
    character_selection_frame.place_forget()
    help_frame.place_forget()
    help_scrollable.place_forget()
    exit_frame.place_forget()
    info_frame.place_forget()
    game_menu_frame.place_forget()
    shop_frame.place_forget()
    inventory_frame.place_forget()
    villager_frame.place_forget()
    battle1_frame.place_forget()

def menu(): #Menu function consists of main options
    hide_frames()
    menu_frame.place(x=0, y=0)
    menu_title_unclickable.place(x=38, y=35)
    play_button.place(x=50, y=145)
    help_button.place(x=50, y=225)
    exit_button.place(x=50, y=305)
    info_button.place(x=302, y=405)

def character_selection(): #Character selection function allows player to select character conveniently
    hide_frames()
    character_selection_frame.place(x=0, y=0)
    character_selection_title_unclickable.place(x=20, y=20)
    character_statistics_label.place(x=140, y=115)
    fenix_button.place(x=20, y=155)
    fenix_stats_label.place(x=130, y=160)
    fenix_info_label.place(x=295, y=165)
    flame_button.place(x=20, y=235)
    flame_stats_label.place(x=140, y=240)
    flame_info_label.place(x=295,y=245)
    flow_button.place(x=20, y=315)
    flow_stats_label.place(x=135, y=320)
    flow_info_label.place(x=295,y=325)
    return_menu_button2.place(x=50, y=405)

def help_menu(): #Called when help button is pressed
    hide_frames()
    help_frame.place(x=0, y=0)
    help_scrollable.place(x=50, y=30)
    return_menu_button.place(x=50, y=405)

def exit_game(): #Exits application when exit button clicked
    hide_frames()
    exit_frame.place(x=0, y=0)
    exit_info_unclickable.place(x= 40, y=200)
    arisen_rpg.after(1000, quit)

def info_menu(): #Information menu provides other information
    hide_frames()
    info_frame.place(x=0, y=0)
    info_unclickable.place(x=87, y=35)
    info_info_label.place(x=50, y=120)
    return_menu_button3.place(x=50, y=405)

"""Determines which character is selected and sets character"""
def fenix_selected():
    global character_selected
    character_selected = fenix.name
    print (character_selected)
    game_menu()

def flame_selected():
    global character_selected
    character_selected = flame.name
    print (character_selected)
    game_menu()

def flow_selected():
    global character_selected
    character_selected = flow.name
    print (character_selected)
    game_menu()

def game_menu(): #Game menu function shows all interactive game options
    hide_frames()
    game_menu_frame.place(x=0, y=0)
    game_menu_title_label.place(x=62, y=3)
    game_menu_scrollable.place(x=30, y=70)
    exit_button2.place(x=315, y=447)
    character_label.place(x=30, y=455)
    if character_selected == fenix.name:
        fenix_label.place(x=150, y=455)
    elif character_selected == flame.name:
        flame_label.place(x=150, y=455)
    elif character_selected == flow.name:
        flow_label.place(x=150, y=455)

def shop_menu(): #Display relevant shop information
    hide_frames()
    shop_frame.place(x=0, y=0)
    shop_scrollable.place(x=40, y=40)
    coins_amount_label.place(x=40, y=330)
    damage_potions_amount_label.place(x=40, y=360)
    health_potions_amount_label.place(x=40, y=390)
    return_game_menu_button.place(x=230, y=430)

def update_shopinventory(): #If an item is purchased from the shop, widgets are configured to adjust to updated amounts
    coins_amount_label.configure(text=f"{coins.item_name}: {coins.amount}")
    damage_potions_amount_label.configure(text=f"{damage_potions.item_name}: {damage_potions.amount}")
    health_potions_amount_label.configure(text=f"{health_potions.item_name}: {health_potions.amount}")

def purchase_damage_potions(): #Purchase damage potions function
    if coins.amount == item1.price or coins.amount > item1.price: #If statement to determine sufficient coins
        print ("Valid")
        print (coins.amount)
        print (damage_potions.amount)
        coins.amount -= 20
        damage_potions.amount += 1
        print (coins.amount)
        print (damage_potions.amount)
        update_shopinventory()
    elif coins.amount == 0 or coins.amount < item1.price:
        print ("Invalid")

def purchase_health_potions(): #Purchase health potions function
    if coins.amount == item2.price or coins.amount > item2.price:
        print ("Valid")
        print (coins.amount)
        print (health_potions.amount)
        coins.amount -= 20
        health_potions.amount += 1
        print (coins.amount)
        print (health_potions.amount)
        update_shopinventory()
    elif coins.amount == 0 or coins.amount < item2.price:
        print ("Invalid")

def update_inventory(): 
    coins_amount_label2.configure(text=f"{coins.item_name}: {coins.amount}")
    damage_potions_amount_label2.configure(text=f"{damage_potions.item_name}: {damage_potions.amount}")
    health_potions_amount_label2.configure(text=f"{health_potions.item_name}: {health_potions.amount}")

def inventory_menu(): #Display user inventory
    hide_frames()
    inventory_frame.place(x=0, y=0)
    inventory_title_unclickable.place(x=45, y=40)
    coins_amount_label2.place(x=45, y=120)
    damage_potions_amount_label2.place(x=45, y=170)
    health_potions_amount_label2.place(x=45, y=220)
    return_game_menu_button2.place(x=230, y=430)
    update_inventory()

def villager_menu(): #Provide player with information
    hide_frames()
    villager_frame.place(x=0, y=0)
    villager_scrollable.place(x=40, y=40)
    return_game_menu_button3.place(x=230, y=430)

def battle1():
    hide_frames()
    battle1_frame.place(x=0, y=0)
    battle1_scrollable.place(x=40, y=40)
    return_game_menu_button4.place(x=230, y=430)

def use_damage_potion():
    if damage_potions.amount > 0:
        print ("Valid")
        damage_potions.amount -= 1
    elif damage_potions.amount == 0 or damage_potions.amount < 0:
        print ("Invalid")

def use_health_potion():
    if health_potions.amount > 0:
        print ("Valid")
        health_potions.amount -= 1
    elif health_potions.amount == 0 or health_potions.amount < 0:
        print ("Invalid")

"""Widgets - Create widgets to be placed on Custom TKinter GUI"""
menu_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
character_selection_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
help_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
exit_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
info_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
game_menu_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
shop_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
inventory_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
villager_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)
battle1_frame = ctk.CTkFrame(arisen_rpg, width=400, height=500)

"""Menu Frame Widgets"""
menu_title_unclickable = ctk.CTkButton(menu_frame, text="Arisen RPG", width=325, height=80, 
                     fg_color="dark red", border_width=2, border_color="dark orange", hover=False, text_color="dark orange", font=("Showcard Gothic", 50, "bold"))

play_button = ctk.CTkButton(menu_frame, text="Play", width=300, height=50, border_width=3, border_color="dark orange", 
                     fg_color="green", text_color="black", font=("Fixedsys", 25, "bold"), command=character_selection)

help_button = ctk.CTkButton(menu_frame, text="Help", width=300, height=50, border_width=3, border_color="dark orange", 
                     fg_color="orange", text_color="black", font=("Fixedsys", 25, "bold"), command=help_menu)

"""Help Frame Widgets"""
help_scrollable = ctk.CTkScrollableFrame(arisen_rpg, width=278, height=300, border_width=2, label_text="Arisen RPG - Information", 
                                         label_font=("Fixedsys", 20), corner_radius=5, bg_color="transparent")
objective_button = ctk.CTkButton(help_scrollable, hover=False, fg_color="dark red", border_width=2, border_color="dark orange", text="Objectives", font=("Fixedsys", 20)).pack(pady=10)
objective_information = "> Traverse the land of\nArisen\n\n> Interact with in-game\nshop, inventory and\nbattles\n\n> Battle the final boss\nfor victory!"
objective_information_label = ctk.CTkLabel(help_scrollable, text=(objective_information), font=("Fixedsys", 20)).pack(pady=10)

features_button = ctk.CTkButton(help_scrollable, hover=False, fg_color="dark red", border_width=2, border_color="dark orange", text="Features", font=("Fixedsys", 20)).pack(pady=10)
features_information = "> Select unique characters\nto battle in-game enemies\n\n> Purchase in-game items\nusing in-game coins\nto assist with battle\n\n> Use special abilities\nin-game during battle"
features_information_label = ctk.CTkLabel(help_scrollable, text=(features_information), font=("Fixedsys", 20)).pack(pady=10)

interaction_button = ctk.CTkButton(help_scrollable, hover=False, fg_color="dark red", border_width=2, border_color="dark orange", text="Interaction", font=("Fixedsys", 20)).pack(pady=10)
interaction_information = "> Press 'Play' to continue\nto character selection\n\n> Press 'Exit' to quit\nArisen RPG\n\n> In character selection,\nselect a character to\nplay as"
interaction_information_label = ctk.CTkLabel(help_scrollable, text=(interaction_information), font=("Fixedsys", 20)).pack(pady=10)

exit_button = ctk.CTkButton(menu_frame, text="Exit", width=300, height=50, border_width=3, border_color="dark orange", 
                     fg_color="red", text_color="black", font=("Fixedsys", 25, "bold"), command=exit_game)
exit_info_unclickable = ctk.CTkButton(exit_frame, text="Exiting...", width=325, height=80, 
                     fg_color="dark red", border_width=2, border_color="dark orange", hover=False, text_color="dark orange", font=("Showcard Gothic", 50, "bold"))

info_button = ctk.CTkButton(menu_frame, corner_radius=100, width=10, height=25, border_width=2, border_color="dark orange", text="i",font=("Fixedsys", 30), command=info_menu)
info_unclickable = ctk.CTkButton(info_frame, border_width=2, border_color="dark orange", hover=False, text="Arisen RPG", font=("Fixedsys", 30))
info_info_label = ctk.CTkLabel(info_frame, text="> Created by: Vincent Hudaja", font=("Fixedsys", 20))

return_menu_button = ctk.CTkButton(help_frame, text="Return", width=300, height=50, border_width=3, border_color="dark orange", 
                     fg_color="dark magenta", text_color="black", font=("Fixedsys", 25, "bold"), command=menu)
return_menu_button2 = ctk.CTkButton(character_selection_frame, text="Return", width=300, height=50, border_width=3, border_color="dark orange", 
                     fg_color="dark magenta", text_color="black", font=("Fixedsys", 25, "bold"), command=menu)
return_menu_button3 = ctk.CTkButton(info_frame, text="Return", width=300, height=50, border_width=3, border_color="dark orange", 
                     fg_color="dark magenta", text_color="black", font=("Fixedsys", 25, "bold"), command=menu)

"""Character Selection Frame Widgets"""
character_selection_title_unclickable = ctk.CTkButton(character_selection_frame, text="Character Selection", width=325, height=80, 
                     fg_color="dark red", border_width=2, border_color="dark orange", hover=False, text_color="dark orange", font=("Showcard Gothic", 30, "bold"))
character_statistics_label = ctk.CTkLabel(character_selection_frame, text=" 💓   |  👊  |   Info", font=("Fixedsys", 20))

fenix_button = ctk.CTkButton(character_selection_frame, text="Fenix", width=100, height=50, border_width=3, border_color="dark red", 
                     fg_color="red", hover_color="dark red", text_color="black", font=("Fixedsys", 25, "bold"), command=fenix_selected)
fenix_stats_label = ctk.CTkLabel(character_selection_frame, text=(f"{fenix.health} {fenix.damage}"), font=("Fixedsys", 30))
fenix_info_label = ctk.CTkLabel(character_selection_frame, text=(f"Balanced"), font=("Fixedsys", 20))

flame_button = ctk.CTkButton(character_selection_frame, text="Flame", width=100, height=50, border_width=3, border_color="dark orange", 
                     fg_color="orange", hover_color="dark orange", text_color="black", font=("Fixedsys", 25, "bold"), command=flame_selected)
flame_stats_label = ctk.CTkLabel(character_selection_frame, text=(f"{flame.health}  {flame.damage}"), font=("Fixedsys", 30))
flame_info_label = ctk.CTkLabel(character_selection_frame, text=(f"+Damage"), font=("Fixedsys", 20))

flow_button = ctk.CTkButton(character_selection_frame, text="Flow", width=100, height=50, border_width=3, border_color="dark blue", 
                     fg_color="blue", hover_color="dark blue", text_color="black", font=("Fixedsys", 25, "bold"), command=flow_selected)
flow_stats_label = ctk.CTkLabel(character_selection_frame, text=(f"{flow.health} {flow.damage}"), font=("Fixedsys", 30))
flow_info_label = ctk.CTkLabel(character_selection_frame, text=(f"+Health"), font=("Fixedsys", 20))

"""Game Menu Widgets"""
game_menu_title_label = ctk.CTkLabel(game_menu_frame, text="Arisen RPG", font=("Showcard Gothic", 50))
game_menu_scrollable = ctk.CTkScrollableFrame(game_menu_frame, width=320, height=300, label_text="Game Menu", label_font=("Fixedsys", 30))

character_label = ctk.CTkLabel(game_menu_frame, text="Character:", font=("Fixedsys", 20))
fenix_label = ctk.CTkLabel(game_menu_frame, text="Fenix", text_color="red", font=("Fixedsys", 20))
flame_label = ctk.CTkLabel(game_menu_frame, text="Flame", text_color="orange", font=("Fixedsys", 20))
flow_label = ctk.CTkLabel(game_menu_frame, text="Flow", text_color="blue", font=("Fixedsys", 20))

"""Shop Frame Widgets"""
shop_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, fg_color="dark magenta", border_width=2, border_color="dark orange", 
                            text="Shop 🛒", font=("Fixedsys", 25),command=shop_menu).pack(pady=10)
shop_scrollable = ctk.CTkScrollableFrame(shop_frame, width=300, height=200, border_width=2, label_text="Arisen RPG - Shop", label_font=("Fixedsys", 25))
shop_instructions_label = ctk.CTkLabel(shop_scrollable, text="> Purchase an item by\n pressing designated button", font=("Fixedsys", 20)).pack(pady=10)
damage_potion_button = ctk.CTkButton(shop_scrollable, width=200, height=50, border_width=2, border_color="dark orange", fg_color="dark red", 
                              text=f"{item1.item_name} 👊⬆- {item1.price} Coins", font=("Fixedsys", 20), command=purchase_damage_potions).pack(pady=10)
health_potion_button = ctk.CTkButton(shop_scrollable, width=200, height=50, border_width=2, border_color="dark orange", fg_color="dark green", 
                              text=f"{item2.item_name} 💓⬆- {item2.price} Coins", font=("Fixedsys", 20), command=purchase_health_potions).pack(pady=10)
coins_amount_label = ctk.CTkLabel(shop_frame, text=f"{coins.item_name}: {coins.amount}", font=("Fixedsys", 20))
damage_potions_amount_label = ctk.CTkLabel(shop_frame, text=f"{damage_potions.item_name}: {damage_potions.amount}", font=("Fixedsys", 20))
health_potions_amount_label = ctk.CTkLabel(shop_frame, text=f"{health_potions.item_name}: {health_potions.amount}", font=("Fixedsys", 20))
return_game_menu_button = ctk.CTkButton(shop_frame, width=50, height=20, border_width=2, border_color="dark orange", fg_color="dark magenta", 
                                        text="Return 🚪", font=("Fixedsys", 25), command=game_menu)

"""Inventory Frame Widgets"""
inventory_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, fg_color="dark blue", border_width=2, border_color="dark orange", 
                                 text="Inventory 💰", font=("Fixedsys", 25), command=inventory_menu).pack(pady=10)
inventory_title_unclickable = ctk.CTkButton(inventory_frame, hover=False, border_width=2, border_color="dark orange", 
                                            text="Arisen RPG - Inventory", text_color="black", font=("Fixedsys", 25))
coins_amount_label2 = ctk.CTkLabel(inventory_frame, text=f"{coins.item_name}: {coins.amount}", font=("Fixedsys", 20))
damage_potions_amount_label2 = ctk.CTkLabel(inventory_frame, text=f"{damage_potions.item_name}: {damage_potions.amount}", font=("Fixedsys", 20))
health_potions_amount_label2 = ctk.CTkLabel(inventory_frame, text=f"{health_potions.item_name}: {health_potions.amount}", font=("Fixedsys", 20))
return_game_menu_button2 = ctk.CTkButton(inventory_frame, width=50, height=20, border_width=2, border_color="dark orange", fg_color="dark magenta", 
                                        text="Return 🚪", font=("Fixedsys", 25), command=game_menu)

"""Villager Frame Widgets"""
villager_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, fg_color="dark red", border_width=2, border_color="dark orange", 
                                text="Villager 🧑", font=("Fixedsys", 25), command=villager_menu).pack(pady=10)
villager_scrollable = ctk.CTkScrollableFrame(villager_frame, width=300, height=290, border_width=2, label_text="Arisen RPG - Villager", label_font=("Fixedsys", 25))
villager_info = "🧑 (Intro): Welcome to the\nland of Arisen RPG!\n\n🧑 (Tip): Purchase potions\nfromthe shop to assist\nin battle!"
villager_info_label = ctk.CTkLabel(villager_scrollable, text=villager_info, font=("Fixedsys", 20)).pack(pady=10)
return_game_menu_button3 = ctk.CTkButton(villager_frame, width=50, height=20, border_width=2, border_color="dark orange", fg_color="dark magenta", 
                                        text="Return 🚪", font=("Fixedsys", 25), command=game_menu)

"""Battle 1 Frame Widgets"""
battle1_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, fg_color="dark green", border_width=2, border_color="dark orange", 
                               text="Battle 1 ⚔️", font=("Fixedsys", 25), command=battle1).pack(pady=10)
battle1_scrollable = ctk.CTkScrollableFrame(battle1_frame, width=300, height=280, border_width=2, label_text="Battle 1 - Spooglin", label_font=("Fixedsys", 25))
use_damage_potion_button = ctk.CTkButton(battle1_scrollable, width=250, height=50, border_width=2, border_color="dark orange", fg_color="dark red", 
                               font=("Fixedsys", 20), text="Use Damage Potion", command=use_damage_potion).pack(pady=10)
use_health_potion_button = ctk.CTkButton(battle1_scrollable, width=250, height=50, border_width=2, border_color="dark orange", fg_color="dark green", 
                               font=("Fixedsys", 20), text="Use Health Potion", command=use_health_potion).pack(pady=10)
return_game_menu_button4 = ctk.CTkButton(battle1_frame, width=50, height=20, border_width=2, border_color="dark orange", fg_color="dark magenta", 
                                        text="Return 🚪", font=("Fixedsys", 25), command=game_menu)

"""Battle 2 Frame Widgets"""
battle2_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, fg_color="dark green", border_width=2, border_color="dark orange", 
                               text="Battle 2 ⚔️", font=("Fixedsys", 25)).pack(pady=10)

"""Battle 3 Frame Widgets"""
battle3_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, fg_color="dark green", border_width=2, border_color="dark orange", 
                               text="Battle 3 ⚔️", font=("Fixedsys", 25)).pack(pady=10)

"""Boss Frame Widgets"""
boss_button = ctk.CTkButton(game_menu_scrollable, width=300, height=50, border_width=2, border_color="dark orange", 
                            text="Boss - Final Battle 🐉", font=("Fixedsys", 25)).pack(pady=10)

game_menu_help_button = ctk.CTkButton(game_menu_frame)
exit_button2 = ctk.CTkButton(game_menu_frame, text="❌", width=20, height=20, border_width=2, border_color="dark orange", 
                     fg_color="red", corner_radius=100, text_color="black", font=("Fixedsys", 25, "bold"), command=exit_game)

def main(): #Main game function
    menu() #Call menu to start
    arisen_rpg.mainloop()

main()
