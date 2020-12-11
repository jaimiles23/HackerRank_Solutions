"""Collection of functions related to navigating directories
"""

##########
# Imports
##########

import os
from typing import Union
from pathlib import Path

from logger.select_chall import logging
import constants
from domains import problem_domains
from git import Repo


##########
# Subdomain dir_name
##########

def get_subdomain_dirname(subdomain_num: int, total_subdomains: int, subdomain: str) -> str:
    """Returns directory name for subdirectory.

    Args:
        subdomain_num (int): Subdomain number
        total_subdomains (int): Total number of subdomains
        subdomain (str): Subdomain name.

    Returns:
        str: directory name
    """
    logging.debug(f"Subdir info: {subdomain_num}, {total_subdomains}, {subdomain}")
    subdomain_num, total_subdomains = str(subdomain_num), str(total_subdomains)
    
    if total_subdomains == '1':     # specific challenges, e.g., 10 days of stats
        subdomain_num = ''
    else:
        while len(subdomain_num) < len(total_subdomains):
            subdomain_num = '0' + subdomain_num
        subdomain_num += '_'

    subdir_name = subdomain_num + subdomain.strip().lower().replace(' ', '_')
    logging.debug(f"subdir - {subdir_name}")
    return subdir_name


##########
# Change dir
##########

def change_dir(domain_dir: str):
    """Changes the current working directory. 
    Creates directory if it doesn't exist.
    Also creates a pre-READMEME.md file.

    Args:
        domain_dir: directory to change to.
    """
    if not os.path.exists( domain_dir):
        logging.info(f"DIR - creating {domain_dir}")
        os.mkdir(domain_dir)
    
    logging.info(f"DIR - changing to {domain_dir}")
    os.chdir(domain_dir)

    return


##########
# get dirname
##########

def get_dirname(dir_path: Path) -> str:
    """returns directory name from windows filepath

    Args:
        dir_path (Path): path oject

    Returns:
        str: directory name
    """
    dirname = str(dir_path.resolve())
    dirname = dirname[dirname.rfind('\\') + 1:]
    logging.debug(f"Dirname {dirname} from {dir_path}")
    return dirname


##########
# get_domain_dirs
##########
def get_domain_dirs(home_dir: object) -> list:
    """Returns list of domain directories.

    Args:
        home_dir (object): Home directory 

    Returns:
        list: List of domain directories
    """
    domain_dirs = []
    for d in problem_domains:
        domain_dir = home_dir / d.name
        domain_dirs.append(domain_dir)
    
    logging.debug("DIR - Domain dirs:" + '\n-'.join(
        [str(d) for d in domain_dirs]))
    return domain_dirs


##########
# get_subdomain_dirs
##########

def get_subdomain_dirs(domain_dir) -> list:
    """Returns list of subdomain dirs.

    Args:
        domain_dir ([type]): Domain directory.

    Returns:
        list: Returns list of subdomain directories.
    """
    not_subdirs = (
        '.ipynb_checkpoints'
    )
    p = Path(domain_dir)
    subdirs = []

    for f in p.glob('**/*'):
        if f.is_dir():
            dir_name = get_dirname(f)
            logging.debug(f"Check dir - {dir_name}")

            if dir_name not in not_subdirs:
                subdirs.append(f)
                
    logging.debug("DIR - Subdomain dirs:" + '\n-'.join(
        [str(d) for d in subdirs]))

    return subdirs


##########
# Challenge csv name
##########

def get_chall_csv_filename(sub_dir) -> str:
    """Returns csv name containing challenge informatin.

    Args:
        sub_dir ([type]): sub directory name

    Returns:
        str: csv filename
    """
    p = Path(sub_dir)

    for f in p.glob('**/*'):
        filename = str(f)
        if filename.endswith(".csv"):
            return filename
    raise Exception(f"No csv located in {sub_dir}")


##########
# pre readme
##########

def make_readme_setup(name: str, url: str):
    """Creates pre-readme in file."""
    filename = constants.PRE_README_FILENAME
    if not os.path.exists( filename):
        with open(filename, 'w') as outfile:
            outfile.write(f"# {name}")
            outfile.write(f"\nContains solutions to [{name}]({url}).")
    return


##########
# Make file
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


##########
# Update github
##########

def update_github(home_dir: object, commit_msg: str) -> None:
    """Updates github directory.

    Args:
        home_dir (object): home dir pathlib
        commit_msg (str): Commit message
    """
    repo = Repo(home_dir)
    repo.git.add(update = True)
    repo.index.commit(commit_msg)
    logging.debug(f"Committing: {commit_msg}")

    origin = repo.remote(name = 'origin')
    origin.push()
    logging.debug("Pushed to repo.")


def get_solution_commit_msg(domain: Path, subdomain: Path, chall_name: str) -> str:
    """Returns commit message for adding solution."""
    domain_name = get_dirname(domain)
    subdomain_name = get_dirname(subdomain)
    return f"Solution to {domain_name} {subdomain_name} - {chall_name}"

