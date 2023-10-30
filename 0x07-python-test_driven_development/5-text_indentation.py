#!/usr/bin/python3
"""
This module contains the function text_indentation which corrects text indentation.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    
    Args:
        text: The text string to be indented.
    
    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ['.', '?', ':']
    for char in special_chars:
        text = text.replace(char, char + '\n\n')
    
    # Splitting the text into lines to strip leading and trailing whitespaces
    lines = text.split('\n')
    for i in range(len(lines)):
        print(lines[i].strip())
