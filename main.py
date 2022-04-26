# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# TODO: add description of this file

import dearpygui.dearpygui as dpg

# Helper function for centering elements horizontally
def centerXPos(frameWidth, elementWidth):
    return frameWidth / 2 - elementWidth / 2

# Initialize variables
viewportWidth = 620
viewportHeight = 850

mainMenuWidth = 600
mainMenuHeight = 800
mainMenuButtonWidth = 450
mainMenuElementSpacing = 50
mainMenuButtonHeight = 30

# Prepare images
dpg.create_context()
logoW, logoH, unused, logoData = dpg.load_image('resources/title_image.png')

with dpg.texture_registry():
    dpg.add_static_texture(logoW, logoH, logoData, tag = 'logo')

# Create main menu
with dpg.window(tag = 'Main Menu', width = mainMenuWidth, height = mainMenuHeight, no_resize = True, no_move = True,
                no_title_bar = True, no_collapse = True, no_close = True, no_saved_settings = True) as window:
    # Add logo
    dpg.add_image('logo', pos = (centerXPos(mainMenuWidth, logoW), mainMenuElementSpacing))
    
    # Add menu options
    with dpg.group(width = mainMenuButtonWidth,
                   pos = (centerXPos(mainMenuWidth, mainMenuButtonWidth), 2 * mainMenuElementSpacing + logoH)):
        # Display all existing projects that can be loaded
        with dpg.child_window(menubar = True, height = 400):
            with dpg.menu_bar():
                with dpg.menu(label = 'Load an existing project:'):
                    pass
            
            # Iterate over all saved projects
            # TODO: Implement project loading feature
            dpg.add_text('Update this part of the GUI once project data can be saved/loaded')
        
        # Display other buttons
        dpg.add_button(label = 'Create New Project', height = mainMenuButtonHeight)
        dpg.add_button(label = 'Close Program', height = mainMenuButtonHeight)

# Finish preparing the window
dpg.create_viewport(title = 'Project Tracker', width = viewportWidth, height = viewportHeight)
dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.set_primary_window('Primary Window', True)

# Start the window
dpg.start_dearpygui()
dpg.destroy_context()
