"""
Class to hold challenge information df & relevant methods.

Loads & stores from csv.
"""

##########
# Imports
##########

import os
import sys

import pandas as pd

from logger.scrape_info import logging

import constants

##########
# Challenge Info
##########

class SavedInfo(object):

    ## Constants
    CSV_FILENAME = constants.CSV_FILE_NOMENCLATURE
    DF_HEADERS = constants.CHALLENGE_INFO_CSV_HEADERS


    def __init__(self, subdomain: str) -> None:
        ## CSV name
        self.CSV_FILENAME = SavedInfo.CSV_FILENAME.format(subdomain).replace(" ", "_").lower()

        self.df = self.load_df()
        self.start_rows = len(self.df)

    
    ##### DataFrame
    def load_df(self) -> "dataframe":
        """Load dataframe into memory.

        Checks if .csv exists, otherwise creates.
        """        
        if os.path.exists(self.CSV_FILENAME):
            logging.debug("DF - loading")
            return pd.read_csv(self.CSV_FILENAME)
        else:
            logging.debug("DF - creating")
            data =  {header: [] for header in self.DF_HEADERS}
            return pd.DataFrame(data)

    def save_df(self) -> None:
        """Saves df to csv."""
        if self.start_rows == len(self.df):
            logging.debug("DF - no changes.")
        else:
            logging.debug("DF - saving changes.")
            self.df.to_csv(
                self.CSV_FILENAME,
                index = False)
        return
    

    ##### Data
    def check_name_in_df(self, challenge_name: str) -> bool:
        """Checks if the challenge naem is in the dataframe.

        Args:
            challenge_name (str): Challenge name

        Returns:
            bool: If name in dataframe.

        NOTE: 
        - Use name because more likely to not change.
        - hackerrank may change order of numbers.
        """
        logging.debug(f"- Locating... {challenge_name}")
        if len(self.df.name) == 0:  # can't check empty df
            return False    
        return self.df.name.str.contains(challenge_name).any()


    def add_entry(
        self,
        parsed_info: object,    # InfoParser - circular import error
        completed: int = 0, 
        todo: int = 1
    ) -> None:
        """Adds entry to the dataframe to save to scs

        Args:
            parsed_info (InfoParser): Information about the challemge
            completed (int, optional): If challenge is completed. Defaults to 0.
            todo (int, optional): If challenge is to be done. Defaults to 1.


        NOTE: Makes a full copy of the data & thus slower performance. 
        Later on, may like to implement so identify all problems that need to be 
        added, and then add them all at once.
        """
        logging.debug(f"- Adding {parsed_info.num} {parsed_info.name} to df")

        data = {
            self.DF_HEADERS[0]  :   parsed_info.num,
            self.DF_HEADERS[1]  :   parsed_info.name,
            self.DF_HEADERS[2]  :   parsed_info.score,
            self.DF_HEADERS[3]  :   parsed_info.difficulty,
            self.DF_HEADERS[4]  :   parsed_info.rate,
            self.DF_HEADERS[5]  :   parsed_info.url,
            self.DF_HEADERS[6]  :   parsed_info.solution_url,
            self.DF_HEADERS[7]  :   completed,
            self.DF_HEADERS[8]  :   todo
        }
        # new_row = pd.DataFrame(data, index = [0])
        self.df = self.df.append(data, ignore_index = True)
        return

