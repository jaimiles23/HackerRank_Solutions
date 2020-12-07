"""
Class to parse challenge information from hackerrank html pages.
"""

##########
# Imports
##########

import pickle
import random
import sys
import time
import webbrowser
from typing import List

from googlesearch import search
from logger.scrape_info import logging

from scrape_info.saved_info import SavedInfo

##########
# HTML parser
##########

class InfoParser(object):
    ## Class constants
    solution_url_BASE = "https://github.com/jaimiles23/HackerRank_Solutions/blob/master/{}/{}/{}"

    ## Instance
    def __init__(
        self, 
        domain: str,
        subdomain: str,
        subdir: str, 
        challenge_num: int, 
        num_challenges: int, 
        filetype: str, 
        text: str, 
        challenge_info: dict,
        saved_info: SavedInfo,
        ):
        """Initializes class with information to write to markdown table.

        Args:
            domain (str): Challenges domain, e.g, statistics or SQL
            subdomain(str): Sub domain, e.g., Basic Select
            subdir (str): Sub-directory, e.g., 1_basic_select
            challenge_num (int): Number Challenges
            num_challenges (int): Total number of challenges
            filetype (str): file extension, e.g., .py
            text (str): Text to parse
            challenge_info (dict): Contains information about challenges. Used for urls to avoid excessive searches.
            saved_info (SavedInfo): Class containing saved challenge information.
        """
        ## Log
        logging.info(f"Parsing information for {domain} - {subdir}, {challenge_num}")
        logging.debug(f"Parsing text:\n\n{text}\n\n")

        ## Directory
        self.domain = domain
        self.subdomain = subdomain
        self.subdir = subdir

        ## Used to create filename
        self.total = str(num_challenges)
        self.num = self.get_challenge_num(challenge_num)
        self.filetype = filetype
        
        ## Text to parse
        self.text = text

        ## Table information
        self.name = self.get_name()
        
        ## Check if challenge already located in dataframe.
        self.chall_saved = saved_info.check_name_in_df(self.name)
        if self.chall_saved:
            logging.debug(f"NOTE: {self.name} already saved\n\n")
            return

        self.filename = self.get_filename()
        self.difficulty = self.get_difficulty()
        self.score = self.get_score()
        self.rate = self.get_rate()
        self.url = self.get_challenge_url(challenge_info, saved_info)
        self.solution_url = self.get_solution_url()


    def get_challenge_num(self, num) -> int:
        """Sets challenge number."""
        num_zeros = len(self.total) - len(str(num))
        num = '0' * num_zeros + str(num)
        logging.debug(f"Challenge num {num}")
        return num


    def get_name(self) -> str:
        """Returns name of problem from text."""
        name = self.text[0: self.text.find("\n")]
        logging.debug(f"Name {name}")
        return name


    def get_filename(self) -> str:
        """Returns file name for hackerrank problem."""
        def remove_special_chars(name: str) -> str:
            """Aux func to remove special characters from file name."""
            special_chars = [' ','<', '>', ':', '"', "'", '/', '\\', '|', '?', '*',]
            for char in special_chars:
                name = name.replace(char, '')
            logging.debug(f'No special chars: {name}')
            return name


        name = remove_special_chars(self.name)
        filename = ''.join([
            self.num,
            "_",
            name.replace(' ', '_').lower(),
            '.',
            self.filetype])
        logging.debug(f"Filename: {filename}")
        return filename


    def get_difficulty(self) -> str:
        """Returns difficulty of problem from text."""
        difficulty = self.text[
            self.text.find("\n") + 1 : self.text.find("Max")
        ]
        difficulty = difficulty if difficulty != 'The challenge is not available yet' else 0        # for locked problems
        logging.debug(f"Difficulty: {difficulty}")
        return difficulty


    def get_score(self) -> str:
        """Returns score of problem from text."""
        score_str, success_str = "Score: ", "Success"
        score = self.text[
            self.text.find(score_str) + len(score_str) : self.text.find(success_str)
        ]
        logging.debug(f"Score: {score}")
        return score


    def get_rate(self) -> str:
        """Returns success rate of problem from text."""
        rate_str = "Rate: "
        rate = self.text[
            self.text.find(rate_str) + len(rate_str) : ]
        logging.debug(f"Rate: {rate}")
        return rate


    def get_challenge_url(self, challenge_info: dict, saved_info) -> str:
        """Returns challenge's url using google library.
        NOTE: Running into HTTP 429 errors. 3 second pause has found success (2 is recommended).
        
        May like to investigate Google-api library:
        https://towardsdatascience.com/current-google-search-packages-using-python-3-7-a-simple-tutorial-3606e459e0d4
        """
        progress_statement = f"Collecting url for {self.name}"
        logging.debug(progress_statement)
        print(progress_statement)

        search_items = "site: hackerrank.com Challenges {}".format(self.name)

        if random.random() < 0.2:
            time.sleep(5)   # arb wait
        
        try:
            urls = search(query= search_items, num = 1, start = 0, stop = 1, pause = 3)
            url = next(urls)
        except Exception as e:
            saved_info.save_df()
            raise Exception(e)

        logging.info(url)
        url = url.replace("/forum", "/problem")
        logging.debug(f"URL: {url}")
        return url
    

    def get_solution_url(self) -> str:
        """Returns url of github solution from text."""
        solution_url = InfoParser.solution_url_BASE.format( 
            self.domain, self.subdir, self.filename)
        logging.debug(f"solution_url: {solution_url}")
        return solution_url

