"""Contains functions related to files
"""

##########
# Imports
##########

import logging
import os

import constants


##########
# Make Readme
##########
def make_readme_setup(name: str, url: str, heading: int):
    """Creates pre-readme in file."""
    filename = constants.PRE_README_FILENAME
    if not os.path.exists( filename):
        with open(filename, 'w') as outfile:
            outfile.write('\n' * 1)
            outfile.write(f"{'#' * heading} {name.title()}")
            outfile.write('\n' * 1)
            outfile.write(f"Contains solutions to HackerRank's [{name}]({url}) challenges.")
            outfile.write('\n' * 2)
            outfile.write('<br/>')
    return


##########
# Make Solution file
##########
def make_file(filename: str, name: str, url: str) -> None:
    """Checks if file exists. If it doesn't exist, creates file."""
    exists = os.path.exists(filename)
    logging.debug(f"{filename} - {exists}")
    if os.path.exists(filename):
        return 
    
    logging.debug(f"FILE - Creating {filename}")
    with open(filename, 'w') as outfile:
        outfile.write(f"Solution to [{name}]({url})")
    return
