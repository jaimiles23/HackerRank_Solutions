"""
Parse html from hackerrank pages.
"""

##########
# Imports
##########

import pickle
import sys
import time
import webbrowser
from typing import List

import bs4
import googlesearch

from logger import logging


##########
# HTML parser
##########


class InfoParser(object):
    ## Class constants
    GITHUB_URL_BASE = "https://github.com/jaimiles23/HackerRank_Solutions/blob/master/{}/{}/{}"


    ## Instance
    def __init__(
        self, 
        domain: str, 
        sub_domain: str, 
        challenge_num: int, 
        num_challenges: int, 
        filetype: str, 
        text: str, 
        challenge_info: dict):
        """Initializes class with information to write to markdown table.

        Args:
            domain (str): Challenges domain, e.g, statistics or SQL
            sub_domain (str): Sub-domain, e.g., SQL's Basic Select
            challenge_num (int): Number Challenges
            num_challenges (int): Total number of challenges
            filetype (str): file extension, e.g., .py
            text (str): Text to parse
            challenge_info (dict): Contains information about challenges. Used for urls to avoid excessive searches.
        """
        ## Log
        logging.info(f"Parsing information for {domain} - {sub_domain}, {challenge_num}")
        logging.debug(f"Parsing text:\n\n{text}\n\n")

        ## Directory
        self.domain = domain
        self.sub_domain = sub_domain

        ## Used to create filename
        self.total = str(num_challenges)
        self.num = self.get_challenge_num(challenge_num)
        self.filetype = filetype
        
        ## Text to parse
        self.text = text

        ## Table information
        self.name = self.get_name()
        self.filename = self.get_filename()
        self.difficulty = self.get_difficulty()
        self.score = self.get_score()
        self.rate = self.get_rate()
        self.url = self.get_challenge_url(challenge_info)
        self.github_url = self.get_github_url()


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


    def get_challenge_url(self, challenge_info: dict) -> str:
        """Returns challenge's url.
        
        NOTE: Some URLS do not follow the specified format. e.g.
            https://www.hackerrank.com/challenges/salary-of-employees for Employee Salaries problem.
                url_base = "https://www.hackerrank.com/challenges/{}/problem"
                name = problem_name.replace(" ", "-")
                return url_base.format(name)

        Instead, I used 3rd party library googlesearch. This is much slower
        NOTE:  HTTPError 429 - Too Many Requests
            > Google uses a rate limiter to stop spamming. Does not specify length of timeout.
        """
        if self.name in challenge_info.keys():
            return challenge_info[self.name]
        
        time.sleep(1/5)     # slow HTTP requests
        search_items = "site: hackerrank.com Challenges {}".format(self.name)
        url = googlesearch.lucky(search_items).replace("/forum", "/problem")   # may return forum/problem
        logging.debug("URL: {url}")
        return url
    

    def get_github_url(self) -> str:
        """Returns url of github solution from text."""
        github_url = InfoParser.GITHUB_URL_BASE.format( 
            self.domain, self.sub_domain, self.filename)
        logging.debug(f"github_url: {github_url}")
        return github_url

