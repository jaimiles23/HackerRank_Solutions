#! env/bin/python

"""
Main script to:

1. Scrape challenge info from urls
2. Parse challenge info
3. Save challenge info to csv
4. Make files for challenge info
"""


##########
# Imports
##########

import os
from pathlib import Path

import aux_funcs
import constants
from challenge_info.domains import problem_domains
from challenge_info.html_parser import InfoParser
from challenge_info.saved_info import SavedInfo
from challenge_info.webpage_info import WebPageInfo
from logger.challenge_info import logging
from challenge_info import logic

# TODO
"""
- Create SEPARATE script to write Csv information to .md

- Create SEPARATE script to randomly select problem & update CSV with input if problem is done.
    - BAT script.
"""

##########
# Main
##########

def main():
    """
    For each domain
        For each subdomain:
            - load subdomain info
            - scrape challenge info
            - parse challenge info
            - save challenge info
            - create relevant file
            - save subdomain info
    """
    ## Home dir
    home_dir = Path(__file__).resolve().parents[1]
    logging.info(f"Directory - Home: {home_dir}")

    ## Driver
    WebPageInfo.start_driver()

    ## Change to domain directory.
    for domain in problem_domains:
        domain_dir = home_dir / domain.name
        aux_funcs.change_dir(domain_dir)

        ## Make readme
        aux_funcs.make_readme_setup(domain.name, domain.total_url)

        ## For each subdomain in Domain
        subdomain_num = 0
        for subdomain, url in domain.info.items():
            ## Change subdomain
            subdomain_num += 1
            subdir = Path( aux_funcs.get_subdomain_dirname(
                subdomain_num, len(domain.info.items()), subdomain))
            aux_funcs.change_dir(subdir)

            ## Make pre-readme file
            aux_funcs.make_readme_setup(subdomain, url)

            ## Load Challenge information
            saved_info = SavedInfo(subdomain)

            ## Scrape challenge information
            challenge_page = WebPageInfo(url = url)

            ## Parse information
            challenge_num = 0
            for challenge in challenge_page.challenge_info:
                is_chall, text = logic.is_challenge(challenge)
                if not is_chall:
                    continue
                
                ## Parse information
                challenge_num += 1
                logging.info(f"Parsing - {challenge_num}")
                logging.debug(text)

                parsed_info = InfoParser(
                    domain= domain.name,
                    subdomain = subdomain,
                    subdir = subdir,
                    challenge_num= challenge_num,
                    num_challenges= len(challenge_page.challenge_info),
                    filetype= domain.filetype,
                    text = text,
                    challenge_info = {},
                    saved_info= saved_info,
                )
            
                ## Make new file & add entry
                if not parsed_info.chall_saved:
                    aux_funcs.make_file(parsed_info.filename,parsed_info.name, parsed_info.url)
                    saved_info.add_entry(parsed_info)

            ## Save subdir information
            saved_info.save_df()

            ## Domain Dir
            logging.info(f"DIR - {domain_dir}")
            os.chdir(domain_dir)

        ## Home dir
        logging.info(f"DIR - {home_dir}")
        os.chdir(home_dir)


##########
# Main
##########
if __name__ == "__main__":
    main()

