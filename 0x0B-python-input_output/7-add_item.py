#!/usr/bin/python3
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Check if the JSON file exists, and load its content if it does
if os.path.isfile('add_item.json'):
    my_list = load_from_json_file('add_item.json')
else:
    my_list = []

# Add command line arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the JSON file
save_to_json_file(my_list, 'add_item.json')
