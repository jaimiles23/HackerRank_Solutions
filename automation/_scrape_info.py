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
from domains import problem_domains
from logger.scrape_info import logging
from scrape_info import file_funcs, logic
from scrape_info.html_parser import InfoParser
from scrape_info.saved_info import SavedInfo
from scrape_info.webpage_info import WebPageInfo


##########
# Main
##########

def scrape_info():
    """
    For each domain:
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
    WebPageInfo.start_driver(home_dir)

    ## Change to domain directory
    for domain in problem_domains:
        domain_dir = home_dir / domain.name
        aux_funcs.change_dir(domain_dir)

        ## Make readme
        file_funcs.make_readme_setup(domain.total_url, domain.name, heading = 1)

        ## For each subdomain in Domain
        subdomain_num = 0
        for subdomain, url in domain.info.items():
            ## Change subdomain
            subdomain_num += 1
            subdir = Path( aux_funcs.get_subdomain_dirname(
                subdomain_num, len(domain.info.items()), subdomain))
            aux_funcs.change_dir(subdir)

            ## Make pre-readme file
            file_funcs.make_readme_setup(url, domain.name, subdomain, heading=2)

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
                    file_funcs.make_file(parsed_info.filename,parsed_info.name, parsed_info.url)
                    saved_info.add_entry(parsed_info)

            ## Save subdir information
            saved_info.save_df()

            ## Domain Dir
            logging.info(f"DIR - {domain_dir}")
            os.chdir(domain_dir)
        
        ## Update repo
        aux_funcs.update_github(home_dir, commit_msg= f"Added challenges for: {domain.name}")

        ## Home dir
        logging.info(f"DIR - {home_dir}")
        os.chdir(home_dir)


##########
# Main
##########
if __name__ == "__main__":
    scrape_info()


