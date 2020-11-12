"""Main script to:
1. Identify & navigate to relevant directories
2. Open relevant webpage
3. Parse HTML for relevant information
4. Save information to pickle file
5. Write information to markdown file
"""

##########
# Imports
##########

import pathlib
import os
from domains import problem_domains
import constants

##########
# Main
##########

def main():

    ## Make all directories in folder
    for domain in problem_domains:
        domain_dir = getattr(domain, constants.DOMAIN)
        if not pathlib.Path.is_dir( domain_dir):
            pathlib.Path.mkdir( domain_dir)




if __name__ == "__main__":
    main()
            
        



    