import os
def clear():
    if(os == 'nt'):
        os.system('cls')
    else:
        os.system('clear')
        
def print_instruction(instruction):
    print("----------------------------------------------------------------------")
    print(instruction)
    print("----------------------------------------------------------------------")

def print_options(menu_list):
    print("======================================================================")
    for x in range(len(menu_list)):
        print(f"[{x + 1}]. {menu_list[x]}")
    print("======================================================================")

class Menu:
    def __init__(self, type, instruction, options):
        self.type = type
        self.instruction = instruction
        self.options = options
    
    def displayMain(self, dir_path):
        clear()
        print("Current default processing path: " + dir_path)
        print_instruction(self.instruction)
        print_options(self.options)
        

class subMenu(Menu):
    def displaySub(self, parent_menu, user_selection):
        clear()
        print(f"Current Selected Menu: {parent_menu.options[user_selection]}")
        print_instruction(self.instruction)
        print_options(self.options)