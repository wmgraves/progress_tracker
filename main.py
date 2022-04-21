# progress_tracker - main.py
# Created by: wmgraves (https://github.com/wmgraves)
# Created on: 4/21/22

# Description:
# TODO: add description of this file

import dearpygui.dearpygui as dpg

# Create primary window
dpg.create_context()

with dpg.window(tag='Primary Window'):
    dpg.add_text('Test text')

# Finish preparing the window
dpg.create_viewport(title='Project Tracker')
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window('Primary Window', True)

# Start the window
dpg.start_dearpygui()
dpg.destroy_context()