# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# TODO: add description of this file

import dearpygui.dearpygui as dpg

# Initialize variables


# Create primary window
dpg.create_context()
with dpg.window(tag='Primary Window') as window:
    
    # Create main menu
    with dpg.group() as main_menu:
        dpg.add_text('Title Image Placeholder')

#     # Create background
#     with dpg.group(label='Background') as backgroundGroup:
#         dpg.add_button(label='test button')

# Finish preparing the window
dpg.create_viewport(title='Project Tracker', width=600, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)

# Start the window
dpg.start_dearpygui()
dpg.destroy_context()
