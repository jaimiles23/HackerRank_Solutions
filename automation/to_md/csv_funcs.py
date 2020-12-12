"""Function to record challenge information
"""
##########
# Imports
##########

import logging

from constants import (CHALL_TBL_COLNAMES, CHALLENGE_INFO_CSV_HEADERS,
                       COL_NB_VIEWER, FULLSCREEN_URL, NB_VIEWER_SOL_TEXT,
                       NB_VIEWER_URL)


##########
# Check 1+ challenges solved
##########
def check_challenge_solved(df: 'dataframe') -> bool:
    """Returns boolean if at least one challenge has been solved.

    Args:
        df (dataframe): dataframe to check

    Returns:
        bool: If 1+ challenges have been solved.
    """
    challenges_solved = df[CHALLENGE_INFO_CSV_HEADERS[-2]].sum()
    if challenges_solved > 0:
        logging.info(f"CHECK - {challenges_solved} challenges solved")
    elif challenges_solved == 0:
        logging.info("CHECK - No challenges solved.")
    else:
        Exception("Challenges solved should be >=0")
    return challenges_solved


##########
# Record challenge info
##########

def record_challenge_info(info_table: 'pw_infotable', df: 'dataframe', nb_viewer: bool = False) -> 'infotable':
    """Returns info table with challenge information added from dataframe.
    """
    def get_star_str(difficulty: str) -> str:
        """Returns star string corresponding to problem difficulty from problem dictionary."""
        star_str = ':star:'
        num_stars = {
            'Easy'      :   1,
            'Medium'    :   2, 
            'Hard'      :   3,
        }
        diff_str = star_str * num_stars.get(difficulty, 0)
        if difficulty == "Multiple Choice Question":
            diff_str = "MC"
        logging.debug(f"{difficulty} - {diff_str}")
        return diff_str if len(diff_str) else '-'


    for index, row in df.iterrows():
        logging.debug(f"Index {index} - adding.")
        if not row[CHALLENGE_INFO_CSV_HEADERS[-2]]: # Not completed
            logging.debug(f"Index {index} - skipping")
            continue

        challenge_text = f"[{row[CHALLENGE_INFO_CSV_HEADERS[1]]}]({row[CHALLENGE_INFO_CSV_HEADERS[5]] + FULLSCREEN_URL})"
        file_extension = (row[CHALLENGE_INFO_CSV_HEADERS[-3]]
                            [row[CHALLENGE_INFO_CSV_HEADERS[-3]].rfind('.') + 1:])
        solution_text = f"[{file_extension}]({row[CHALLENGE_INFO_CSV_HEADERS[-3]]})"

        ## Num, chall_text, score, difficulty, rate, sol_text
        row_dict = {
            CHALL_TBL_COLNAMES[0] :   row[CHALLENGE_INFO_CSV_HEADERS[0]],
            CHALL_TBL_COLNAMES[1] :   challenge_text,
            CHALL_TBL_COLNAMES[2] :   row[CHALLENGE_INFO_CSV_HEADERS[2]],
            CHALL_TBL_COLNAMES[3] :   get_star_str(row[CHALLENGE_INFO_CSV_HEADERS[3]]),
            CHALL_TBL_COLNAMES[4] :   row[CHALLENGE_INFO_CSV_HEADERS[4]],
            CHALL_TBL_COLNAMES[5] :   solution_text,
        }
        ## IF NB viewer == True
        if nb_viewer:
            row_dict[COL_NB_VIEWER] = get_nbviewer_sol_text(row[CHALLENGE_INFO_CSV_HEADERS[-3]])

        info_table.add_entry(row_dict)
    return info_table


def get_nbviewer_sol_text(solution_url) -> str:
    """Returns text to write into table for notebook solution

    Args:
        solution_url ([type]): url for github solution
    Returns:
        str: text for github solution
    """
    replace_components = (
        "https://",
        ".com",
    )
    for component in replace_components:
        solution_url = solution_url.replace(component, '')
    
    nb_solution_url = NB_VIEWER_URL + solution_url
    return f"[{NB_VIEWER_SOL_TEXT}]({nb_solution_url})"
    
