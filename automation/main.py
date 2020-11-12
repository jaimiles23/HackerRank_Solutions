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

from pathlib import Path
import os
from domains import problem_domains


##########
# Main
##########

def main():

    home_dir = Path(__file__).resolve().parents[1]

    ## All domain directories exist
    for domain in problem_domains:
        new_dir = Path(domain.name)

        if not Path.is_dir(new_dir):
            print(f"Creating dir for: {new_dir}")
            os.mkdir(new_dir)
    

    for domain in problem_domains:
        os.chdir( home_dir / domain.name)

        for subdir, url in domain.info.items():
            print(subdir, url)
            subdir = subdir.replace(' ', '_')

            if not Path.is_dir(subdir):
                print(f"Creating dir for: {subdir}")
                os.mkdir(subdir)
            
            ## TODO: open browser for URL

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

