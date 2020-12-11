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
import aux_funcs


##########
# Get input
##########

def get_input() -> List[str,]:
    """Returns user input for _get_challenge script

    Returns:
        List[str,]: List of strings representing input.
    """
    args = sys.argv[1:]
    logging.debug(f"SYS ARGS: {sys.argv[1:]}")
    for i in range(len(args)):
        args[i] = constants.INPUT_CHALL_DOMAIN.get(args[i], args[i])
    return args

##########
# Clean dirs
##########

def clean_dirs(user_args: list, domain_dirs: list):
    logging.info(f"CLEAN DIRS - user_args {user_args}, domain_dirs {domain_dirs}")

    deleted_dirs = 0
    for i in range(len(domain_dirs)):
        domain = domain_dirs[i - deleted_dirs]
        dirname = aux_funcs.get_dirname(domain)

        logging.debug(f"CHECK DIR -  {dirname}")
        flag_domain_in_args = (dirname in user_args)

        if not flag_domain_in_args:
            logging.debug(f"DEL DIR - {dirname} not in user_args {user_args}")
            del domain_dirs[i - deleted_dirs]
            deleted_dirs += 1
    
    if not len(domain_dirs):
        raise Exception("No directories remain!")
    return domain_dirs


##########
# Ask Questions
##########

def ask_question(question: str) -> bool:
    """Asks the user a yes/no question. Returns boolean, 1 & 0 respectively.
    """
    answers = ('y', 'n')
    while (a := input(question).lower().strip()) not in answers:
        continue

    if a == answers[0]:
        return True
    return False


def ask_solved_chall() -> bool:
    """Returns boolean if user solved challenge or not."""
    question = "Did you solve the challenge? (y/n): "
    return ask_question(question)


def ask_todo() -> bool:
    """Asks the user if challenge should stay on TODO list."""
    question = "Should the question stay on TODO list? (y/n): "
    return ask_question(question)


def ask_next_chall() -> bool:
    """Asks the user if they want to complete another challenge

    Returns:
        bool: If user wants to complete another challenge
    """
    question = "Complete another challenge? (y/n): "
    return ask_question(question)

