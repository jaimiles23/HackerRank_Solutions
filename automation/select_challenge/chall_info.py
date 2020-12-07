"""Functions for checking challenge information
"""
##########
# Imports
##########

import os
import webbrowser
from typing import Tuple

import pandas as pd
from constants import CHALLENGE_INFO_CSV_HEADERS
from logger.select_chall import logging
from scrape_info.webpage_info import WebPageInfo

##########
# Locate Challenge
##########

def locate_challenge(df: 'dataframe') -> Tuple[bool, int]:
    """Returns boolean indicating if challenge located & index of challenge information

    Args:
        df (dataframe): dataframe of challenge inforamtion

    Returns:
        Tuple[bool, int]: Challenge located, index of challenge information
    """
    for index, row in df.iterrows():
        logging.debug(f"CHECK - Index {index}")

        if (
            row[CHALLENGE_INFO_CSV_HEADERS[-1]] and     ## TODO
            not row[CHALLENGE_INFO_CSV_HEADERS[-2]]     ## Completed
        ):
            logging.info(f"FOUND - challenge at {index}")
            return (True, index)
    return (False, None)


##########
# Open files to solve challenge
##########

def solve_challenge(df: 'dataframe', index: int) -> bool:
    """Opens challenge url & file for user to complete.

    Args:
        df (dataframe): dataframe containing information
        index (int): Row to read
    
    Returns:
        bool: if challenge was solved.
    """
    logging.info(f"Chall info for:  {index}")
    chall_info = df.iloc[index]
    logging.info(f"INFO: {chall_info}")

    ## Solution file
    solution_url = url = chall_info[CHALLENGE_INFO_CSV_HEADERS[-3]]
    print(solution_url)
    sol_filename = solution_url[ solution_url.rfind('/') + 1:].encode('unicode-escape').decode()
    print(sol_filename)
    logging.info(f"sol filename {sol_filename}")
    os.system(sol_filename)


    ## Open url
    url = chall_info.loc[CHALLENGE_INFO_CSV_HEADERS[-4]]
    logging.debug(f"url: {url}")
    WebPageInfo(url, scrape= False)

    return


##########
# Get challenge name
##########
def get_chall_name(df: 'dataframe', index: int) -> str:
    """Returns challenge name."""
    chall_info = df.iloc[index]
    name = ' '.join([str(index), '-', chall_info.loc[CHALLENGE_INFO_CSV_HEADERS[1]]])
    logging.debug(f"Chall name {name}")
    return name
    


##########
# Mark Completed
##########
def mark_completed(df: 'dataframe', index: int, name: str) -> None:
    """Marks challenge index as completed in dataframe.

    Args:
        df (dataframe): df
        index (int): challenge index
        name (str): challenge name
    """
    msg_completed = f"Logging index {name} as completed"

    logging.info(msg_completed)
    df.at[index, CHALLENGE_INFO_CSV_HEADERS[-2]] = 1
    return


##########
# Mark NOT todo
##########
def mark_not_todo(df: 'datamframe', index: int, name: str) -> None:
    """marks challenge as not todo in dataframe.

    Args:
        df (datamframe): df
        index (int): challenge index
        name (str): challenge name
    """
    msg_not_todo = f"Marking NOT todo for: {name}"

    logging.info(msg_not_todo)
    print(msg_not_todo)
    
    df.at[index, CHALLENGE_INFO_CSV_HEADERS[-1]] = 0
    return
