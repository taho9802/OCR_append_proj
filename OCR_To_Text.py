from PIL import Image, ImageEnhance
import pytesseract
import os
from datetime import datetime
from Menu import Menu, subMenu

"""
def setup_menu(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    menus = []  # List to store all the menu objects
    instruction = ""
    options = []
    current_type = ""  # Keep track of the current menu type being processed
    
    for line in lines:
        line = line.strip()
        if line.startswith("MAIN") or line.startswith("SUB"):
            # If options have been gathered for a previous menu, add that menu to the list
            if options:
                # Decide whether to create a Menu or subMenu based on current_type
                if current_type == "MAIN":
                    menus.append(Menu(current_type, instruction, options))
                else:
                    menus.append(subMenu(current_type, instruction, options))
                # Reset for the next menu
                options = []
            current_type = line
        elif line.startswith("-i"):
            instruction = line[3:]  # Get instruction text
        elif line.startswith("-o"):
            options.append(line[3:])  # Add option to the options list

    # Add the last menu to the list after processing all lines
    if options:
        # Decide whether to create a Menu or subMenu based on current_type
        if current_type == "MAIN":
            menus.append(Menu(current_type, instruction, options))
        else:
            menus.append(subMenu(current_type, instruction, options))

    return menus

def run_menu_system(menus, directory):
    menu_stack = [0]  # Start with the index of the main menu
    while True:
        current_menu_index = menu_stack[-1]  # Get the current menu index
        current_menu = menus[current_menu_index]

        # Display the current menu
        if isinstance(current_menu, Menu):
            current_menu.displayMain(directory)
        else:
            # Additional handling for subMenus if needed
            pass  # Example placeholder, adjust as needed

        # Get user input
        selection = input("Select an option (number), or type 'cancel' to go back: ").strip().lower()

        # Handle 'cancel' command to go back
        if selection == 'cancel':
            if len(menu_stack) > 1:
                menu_stack.pop()  # Go back to the previous menu
                continue
            else:
                print("No previous menu to return to.")
                continue

        try:
            selection_index = int(selection) - 1
            if 0 <= selection_index < len(current_menu.options):
                print(f"You selected: {current_menu.options[selection_index]}")
                
                # Implement navigation or specific action based on the selected option
                # Check if the selection corresponds to a submenu
                if isinstance(current_menu, Menu) and current_menu.type == "MAIN" and hasattr(current_menu, 'submenus'):
                    # Assuming each main menu knows its submenus
                    submenu_indices = current_menu.submenus  # Placeholder for where submenu indices are stored
                    if selection_index in submenu_indices:
                        menu_stack.append(submenu_indices[selection_index])
                        continue

                # For actions like "Process files", directly call the function here
                # if current_menu.options[selection_index].lower() == "process files":
                #     process_files_function()

            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Please enter a valid number.")



"""
def extract_datetime_from_filename(filename):
    # Extract timestamp part from filename
    timestamp_str = filename.replace("Screenshot ", "").split(".png")[0]
    # Define the format of the timestamp in the filename
    timestamp_format = "%Y-%m-%d at %I.%M.%S %p"
    # Convert string to datetime object
    return datetime.strptime(timestamp_str, timestamp_format)

# Function to perform OCR on all PNG files in a specified directory and append the results to a text file
def png_to_text_with_contrast_enhancement_sorted(directory, output_file, contrast_factor=1.5):
    
    # List all PNG files
    png_files = [f for f in os.listdir(directory) if f.endswith('.png')]
    # Sort files by datetime extracted from their filenames
    png_files_sorted = sorted(png_files, key=extract_datetime_from_filename)
    
    with open(output_file, 'a') as outfile:  # Open the output file in append mode
        output_history = []
        for file in png_files_sorted:
            file_path = os.path.join(directory, file)
            try:
                term_output = f"Processing {file} with enhanced contrast..."
                print(term_output,end='')
                # Open the image file
                img = Image.open(file_path)
                # Enhance contrast
                enhancer = ImageEnhance.Contrast(img)
                enhanced_img = enhancer.enhance(contrast_factor)
                
                # Perform OCR
                text = pytesseract.image_to_string(enhanced_img)
                outfile.write(text + "\n")
                print("               done.")
                term_output += term_output + "               done."
                output_history.append(term_output)
            except Exception as e:
                print(f"Error processing {file}: {e}")
"""
def clearScreen():
    if( os == 'nt'):
        os.system('cls')
    else:
        os.system('clear')
        
        
def main():
    clearScreen()
    print("Starting Program")
    directory = ""
    try:
        with open('directory_path.txt', 'r') as file:
            directory = file.read().strip()
            print(f"Default processing path: {directory}")
    except FileNotFoundError:
        print("Directory file not found. Setting up a new default directory.")
        directory = input("Enter the default directory path: ")
        with open("directory_path.txt", 'w') as file:
            file.write(directory)
        print(f"Default path set to: {directory}")
    menues = setup_menu("config/menu_data.txt")
    run_menu_system(menues, directory)
"""

        
        


directory = '/Users/taewoohong/School/24Spring_A/ENG/Week5/Critical Reading Strategies/Images'
output_file = 'output.txt'
png_to_text_with_contrast_enhancement_sorted(directory, output_file)
    
#main()9802
