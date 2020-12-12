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
def make_readme_setup(url: str,  domain: str, subdomain: str = None, heading: int = 1):
    """Creates pre-readme in file."""
    filename = constants.PRE_README_FILENAME
    if os.path.exists( filename):
        return

    section_title = subdomain if subdomain else domain
    if subdomain:
        msg = f"Contains solutions to HackerRank's {domain} [{subdomain}]({url}) challenges."
    else:
        msg = f"Contains solutions to HackerRank's [{domain}]({url}) challenges."

    logging.debug(f"DIR - {section_title} Creating pre-readme.")
    with open(filename, 'w') as outfile:
        outfile.write('\n' * 1)
        outfile.write(f"{'#' * heading} {section_title.title()}")
        outfile.write('\n' * 1)
        outfile.write(msg)
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
