"""Functions for checking challenge information
"""
##########
# Imports
##########

import os
import webbrowser
from typing import Tuple

import pandas as pd
from constants import CHALLENGE_INFO_CSV_HEADERS, FULLSCREEN_URL
from logger.select_chall import logging
from scrape_info.webpage_info import WebPageInfo


##########
# Locate Challenge
##########

def locate_challenge(df: 'dataframe', last_chall_index: int, flag_review: bool) -> Tuple[bool, int]:
    """Returns boolean indicating if challenge located & index of challenge information

    Args:
        df (dataframe): dataframe of challenge inforamtion

    Returns:
        Tuple[bool, int]: Challenge located, index of challenge information
    """
    if flag_review:
        df = df.sample(frac=1).reset_index(drop=True)

    for index, row in df.iterrows():
        logging.debug(f"CHECK - Index {index}")

        if (
            row[CHALLENGE_INFO_CSV_HEADERS[-1]] and                 ## TODO
            row[CHALLENGE_INFO_CSV_HEADERS[-2]] == flag_review and  ## Completed = flag_review
            index != last_chall_index
        ):
            logging.info(f"FOUND - challenge at {index}")
            return_index = row[CHALLENGE_INFO_CSV_HEADERS[0]] if flag_review else index
            return (True, return_index)
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
    sol_filename = solution_url[ solution_url.rfind('/') + 1:]

    logging.info(f"sol filename {sol_filename}")
    print(f"File: {sol_filename}")
    os.system(sol_filename)

    ## Open url
    url = chall_info.loc[CHALLENGE_INFO_CSV_HEADERS[-4]] + FULLSCREEN_URL
    logging.debug(f"url: {url}")
    print(f"Webpage: {url}")
    WebPageInfo(url, scrape= False)

    return


##########
# Get challenge name
##########
def get_chall_name(df: 'dataframe', index: int) -> str:
    """Returns challenge name."""
    chall_info = df.iloc[index]
    name = ' '.join([str(index + 1), '-', chall_info.loc[CHALLENGE_INFO_CSV_HEADERS[1]]])
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
