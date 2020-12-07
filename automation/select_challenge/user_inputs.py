"""Auxiliary functions for the _get_challenge script
"""

##########
# Imports
##########

import logging
import os
import random
import sys
from typing import List

import constants


##########
# Get input
##########

def get_input() -> List[str,]:
    """Returns user input for _get_challenge script

    Returns:
        List[str,]: List of strings representing input.
    """
    args = sys.argv[1:]
    for i in range(len(args)):
        args[i] = constants.INPUT_CHALL_DOMAIN.get(i, args[i])
    
    return args

##########
# Clean dirs
##########

def clean_dirs(user_args: list, domain_dirs: list):
    logging.info(f"CLEAN DIRS - user_args {user_args}, domain_dirs {domain_dirs}")

    deleted_dirs = 0
    for i in range(len(domain_dirs)):
        domain = str(domain_dirs[i - deleted_dirs].resolve())
        domain = domain[domain.rfind('\\') + 1:]
        print(domain)
        
        if domain not in user_args:
            del domain_dirs[i - deleted_dirs]
            deleted_dirs += 1
    
    if not len(domain_dirs):
        raise Exception("No directories reamining!")
    return domain_dirs


##########
# Solved challenge
##########

def ask_solved_chall() -> bool:
    """Returns boolean if user solved challenge or not."""
    answers = ('y', 'n')
    question = "Did you solve the challenge? (y/n): "
    while (a := input(question).lower().strip()) not in answers:
        continue

    if a == answers[0]:
        return True
    return False


##########
# Ask TODO
##########

def ask_todo() -> bool:
    """Asks the user if challenge should stay on TODO list."""
    answers = ('y', 'n')
    question = "Should the question stay on TODO list? (y/n): "
    while (a := input(question).lower().strip()) not in answers:
        continue

    if a == answers[0]:
        return True
    return False


