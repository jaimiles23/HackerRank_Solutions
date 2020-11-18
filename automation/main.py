"""Main script to:
1. Identify & navigate to relevant directories
2. Open relevant webpage
3. Parse HTML for relevant information
4. Save information to pickle file
5. Write information to markdown file
"""
## TODO: Add to geckdriver to path -- currently in users.
import sys

for x in sys.path:
    print(x)

##########
# Imports
##########

from pathlib import Path
import os
from domains import problem_domains
import dir_functions
from logger import logging
from webpage import WebPage
import constants

##########
# Main
##########

def main():

    home_dir = Path(__file__).resolve().parents[0]
    logging.debug(f"Home dir: {home_dir}")

    ## All domain directories exist
    for domain in problem_domains:
        new_dir = Path(domain.name)

        if not Path.is_dir(new_dir):
            logging.debug(f"Creating dir for: {Path() / new_dir}")
            os.mkdir(new_dir)
    

    for domain in problem_domains:
        os.chdir( home_dir / domain.name)

        for subdomain, url in domain.info.items():
            subdir = Path( dir_functions.get_subdomain_dirname(subdomain))

            if not Path.is_dir(subdir):
                logging.debug(f"Creating dir for: {Path(subdir)}")
                os.mkdir(subdir)
            
    
            ## TODO: open browser for URL
            webpage = WebPage(url = url, locate_by = constants.LOCATE_BY, identifier = constants.PROBLEM_CLASS) 
            subdomain_info = webpage.get_info()

            ## TODO: Webscrape information

            ## TODO: Save information to pickle file

            ## TODO: Write to markdown

            ## TODO: Back up to domain dir

        
        ##TODO Back up to home_dir
        os.chdir(home_dir)
            


        
    
            





##########
# Main
##########

if __name__ == "__main__":
    main()

