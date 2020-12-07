"""
Script to write challenge information to markdown file.

1. Check each directory. 
2. Check each sub directory.
3. If there is a CSV that ends with _info.csv, read dataframe and append to READM.md
4. Also write other information to markdown readme, etc.
    -- may be easier just to make copy of pre-readme file & append to that.

"""


##########
# Imports
##########

import os
from pathlib import Path
import shutil

import pandas as pd
import pywrangle as pw

import aux_funcs
import constants
from logger.write_to_md import logging
from to_md.csv_funcs import record_challenge_info, check_challenge_solved
from to_md import readme_funcs


##########
# Main
##########

def write_to_md():
    """
    For each domain:
        For each subdomain: 
            - load _info.csv
            - add to pywrangle table
            - write to README.md
            - write all subdomains to master domain README.md
    """
    ## Home dir 
    home_dir = Path(__file__).resolve().parents[1]
    logging.info(f"DIR - Home: {home_dir}\n")

    ## Domain dirs
    domain_dirs = aux_funcs.get_domain_dirs(home_dir)

    ## Home readme
    readme_contents, readme_toc = readme_funcs.get_readme_helper_filenames(home_dir)
    readme_funcs.create_file(readme_contents)
    readme_funcs.create_file(readme_toc, header= "Table of Contents")

    for domain_dir in domain_dirs:
        domain_toc = True
        aux_funcs.change_dir(domain_dir)

        domain_prereadme, domain_readme = readme_funcs.get_readme_names(domain_dir)
        shutil.copy(domain_prereadme, domain_readme)
        subdomain_dirs = aux_funcs.get_subdomain_dirs(domain_dir)
        
        for sub_dir in subdomain_dirs:
            aux_funcs.change_dir(sub_dir)

            ## Make readme. md & write to
            subdomain_prereadme, subdomain_readme = readme_funcs.get_readme_names(sub_dir)
            shutil.copy(subdomain_prereadme, subdomain_readme)

            ## Read table
            infotbl_subdomain = pw.TableInfo(constants.CHALL_TBL_COLNAMES)
            csv_filename = aux_funcs.get_chall_csv_filename(sub_dir)
            df = pd.read_csv(csv_filename)
            
            if not check_challenge_solved(df):
                continue

            ## Write to file
            infotbl_subdomain = record_challenge_info(infotbl_subdomain, df)
            readme_funcs.write_newline(subdomain_readme)
            infotbl_subdomain.print_info(
                markdown=True,
                show_records_col= False,
                md_filename= subdomain_readme,
                write_type= 'a'
            )
            readme_funcs.write_toc_link(subdomain_readme)
            readme_funcs.write_in_to_out_file(subdomain_readme, domain_readme)

            ## Write to TOC
            if domain_toc:
                readme_funcs.write_to_toc_file(domain_dir, 1, readme_toc)
                domain_toc = False
            readme_funcs.write_to_toc_file(sub_dir, 2, readme_toc)
            

        readme_funcs.write_in_to_out_file(domain_readme, readme_contents)
    
    ## home readme
    home_prereadme, home_readme = readme_funcs.get_readme_names(home_dir)
    shutil.copy(home_prereadme, home_readme)
    readme_funcs.write_in_to_out_file(readme_toc, home_readme)
    readme_funcs.write_in_to_out_file(readme_contents, home_readme)
    return



if __name__ == "__main__":
    write_to_md()



