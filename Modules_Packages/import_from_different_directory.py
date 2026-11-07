# when we want to import modules from different destination
import sys
import os

# Add the path of the different folder to sys.path
# Replace 'path/to/your/folder' with the actual relative or absolute path
folder_path = os.path.abspath('path/to/your/folder')
sys.path.append(folder_path)

# Now you can import your module
import my_module

# Use a function or class from the imported module
my_module.my_function()