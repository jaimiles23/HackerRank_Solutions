"""Script to return hackerrank challenge to complete.
- Challenges are selected from CSVs that are marked "TODO" and not "Completed"
- The user may also provide 2 additional parameters:
    - domain of problem
    - if problem is new (default) or review.
        NOTE: need to completely change script for review...


## TODO:
    1. Write BAT script
    2. Test BAT script with different directories
    3. Test BAT script with review option
        - just need to randomly select option from DF.
        NOTE: saved reviewed problems in pickle file. 
        If saved files are chosen, continue in for loop?
"""

##########
# Imports
##########

import random
from pathlib import Path

import pandas as pd

import _write_to_md
import aux_funcs
import constants
from logger.select_chall import logging
from scrape_info.webpage_info import WebPageInfo
from select_challenge import chall_info, user_inputs

##########
# Main
##########

def start_challenge():
    home_dir = Path(__file__).resolve().parents[1]
    domain_dirs = aux_funcs.get_domain_dirs(home_dir)

    ## Inputs
    user_args = user_inputs.get_input()
    if len(user_args) and user_args[0] != constants.INPUT_REVIEW:
        domain_dirs = user_inputs.clean_dirs(user_args, domain_dirs)

    ## Review
    if constants.INPUT_REVIEW in user_args:
        random.shuffle(domain_dirs)
    
    ## Driver
    WebPageInfo.start_driver(home_dir)

    ## Begin tree recursion
    for domain_dir in domain_dirs:
        aux_funcs.change_dir(domain_dir)
        subdomain_dirs = aux_funcs.get_subdomain_dirs(domain_dir)

        if constants.INPUT_REVIEW in user_args:
            random.shuffle(subdomain_dirs)
        
        for sub_dir in subdomain_dirs:
            print(domain_dir, sub_dir)
            aux_funcs.change_dir(sub_dir)

            ## Read CSV
            csv_filename = aux_funcs.get_chall_csv_filename(sub_dir)
            df = pd.read_csv(csv_filename)

            flag_challenge, index = True, float('inf')
            while flag_challenge:   # continue
                ## Locate Challenge
                flag_challenge, index = chall_info.locate_challenge(df, index)
                
                ## Open challenge url & file with vscode
                if flag_challenge:
                    chall_name = chall_info.get_chall_name(df, index)
                    chall_info.solve_challenge(df, index)

                    solved = user_inputs.ask_solved_chall()
                    if solved:
                        chall_info.mark_completed(df, index, chall_name)

                    else:
                        flag_todo = user_inputs.ask_todo()
                        if not flag_todo:
                            chall_info.mark_not_todo(df, index, chall_name)
                    
                    if solved or not flag_todo:
                        logging.info(f"Saving {csv_filename}")
                        df.to_csv(csv_filename, index = False)

                    if solved:
                        _write_to_md.write_to_md()
                        commit_msg = aux_funcs.get_solution_commit_msg(domain_dir, sub_dir, chall_name)
                        aux_funcs.update_github(home_dir, commit_msg)

                    if not user_inputs.ask_next_chall():
                        return
    
    print("Did not locate a challenge.")
    ## TODO: make different message for review & regular



if __name__ == "__main__":
    start_challenge()

