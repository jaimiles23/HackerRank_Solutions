"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 12:31:54
 * @modify date 2020-09-06 14:12:15
 * @desc [
    Script to webscrape hackerrank problems and format them into markdown table.

    1. Create meta list of problem information
        1. Scrape problem name, difficulty, and score from page.
        2. Construct URL
    2. For each problem
        1. Create python file with problem name and link to URL
        2. Construct future github address
        3. Create line in markdown file
    

    Usage:
    - Change HACKERRANK_WEBPAGE and run
    - CHECK ALL URLS
        - Some URLS do not follow the specified format. e.g.
        https://www.hackerrank.com/challenges/salary-of-employees for Employee Salaries problem.
 ]
 */
"""

##########
# Constants
##########
"""
This section changes constants processed by the script.
"""

## Website
HACKERRANK_WEBPAGE = "https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=select"
DOMAIN = "01_basic_select"      # used to create github url.
SOLUTION_FILENAME = "MySQL"

## HTML identifiers
PROBLEM_CLASS = 'challengecard-title' # class
PROBLEM_TAG = 'h4'                # tag

## location method
LOCATE_BY = "class"


##########
# Imports
##########

import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


##########
# Driver
##########

def get_driver() -> object:
    """Returns Selenium driver object.

    NOTE: If running the remote driver, need to create standalone server. 
    Run the following command on cmd
        >>> java -jar selenium-server-standalone-3.141.0.jar -port 4446
    """
    ## Desktop
    driver = webdriver.Firefox()

    ## Remote server
    # driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4446/wd/hub',
    #     desired_capabilities=DesiredCapabilities.FIREFOX)
    
    driver.get(HACKERRANK_WEBPAGE)
    return driver


def get_elements( driver: object, identifier: str, LOCATE_BY: str) -> list:
    """Auxiliary method to get list of elements with identifier."""

    for _ in range(5):
        time.sleep(1)       # NOTE: Need timer so whole page loads.
        
        if LOCATE_BY == "class":
            output = driver.find_elements_by_class_name(identifier)
        elif LOCATE_BY == "tag":
            output = driver.find_elements_by_tag_name(identifier)

        if len(output):
            return output
        
        time.sleep(0.1)     # Table may not load immediately, try 5x
    
    raise Exception("Could not locate elements!")


##########
# Get info
##########

def get_problem_info(problems: list) -> List[dict]:
    """Parses information from problems into a list of dictionaries.

    Contains auxiliary methods to parse inforation from problem text.
    """

    ########## Auxiliary Functions

    def _get_name(text: str) -> str:
        """Returns name of problem from text."""
        return text[0:
            text.find("\n")]
    

    def _get_file_name(num_problems: int, problem_num: int, name: str) -> str:
        """Returns file name for hackerrank problem."""
        num_problems, problem_num = str(num_problems), str(problem_num)

        while len(num_problems) != len(problem_num):
            problem_num = '0' + problem_num
        
        file_name = '_'.join([
            problem_num,
            name.replace(' ', '_').lower()
        ])
        return file_name
    

    def _get_difficulty(text: str) -> str:
        """Returns difficulty of problem from text."""
        return text[
            text.find("\n") + 1 : text.find("Max")
        ]


    def _get_score(text: str) -> str:
        """Returns score of problem from text."""
        score_str = "Score: "
        success_str = "Success"
        return text[
            text.find(score_str) + len(score_str) : text.find(success_str)
        ]
    

    def _get_rate(text: str) -> str:
        """Returns success rate of problem from text."""
        rate_str = "Rate: "
        return text[
            text.find(rate_str) + len(rate_str) : ]
    

    def _get_problem_url(problem_name: str) -> str:
        """Returns url of challenge problem from text."""
        url_base = "https://www.hackerrank.com/challenges/{}/problem"
        name = problem_name.replace(" ", "-")
        return url_base.format(name)
    

    def _get_github_url(file_name: str) -> str:
        """Returns url of github solution from text.
        https://github.com/jaimiles23/hacker_rank/blob/master/sql/01_basic_select/01_revising_select_query_I.sql
        """
        github_url_base = "https://github.com/jaimiles23/hacker_rank/blob/master/sql/{}/{}"
        return github_url_base.format(DOMAIN, file_name)


    ########## Create list of dictionaries
    problem_dicts = list()
    problem_num = 0
    
    for p in problems:
        ## vars for dict
        text = p.text
        problem_num += 1
        problem_dict = dict()

        ## vars for functions
        problem_name = _get_name(text)
        num_problems = len(problems)
        file_name = _get_file_name(num_problems, problem_num, problem_name)

        ## create dict
        problem_dict = {
            'num'           :   str(problem_num),
            'name'          :   problem_name,
            'file_name'     :   file_name,
            'difficulty'    :   _get_difficulty(text),
            'score'         :   _get_score(text),
            'rate'          :   _get_rate(text),
            'problem_url'   :   _get_problem_url(problem_name),
            'github_url'    :   _get_github_url(file_name),
        }
        problem_dicts.append(problem_dict)
    
    return problem_dicts


##########
# Print Markdown columns
##########

def create_md_row(problem_dicts: list) -> None:
    """Prints rows for hacker_rank README.md markdown table for the specified problems.
    
    Markdown table headers as follow:
    Name    |   Challenge   |   Score   |   Difficulty  |   Rate    |   Solution
    """
    star_str = ":star:"
    num_stars = {
        'Easy'      :   1,
        'Medium'    :   2, 
        'Hard'      :   3,
    }
    link_text_str = "[{}]({})"

    for problem in problem_dicts:
        row_join = "\t|\t"
        row_contents = [
            problem['num'],
            link_text_str.format( problem['name'], problem['problem_url']),
            problem['score'],
            star_str * num_stars[ problem['difficulty']],
            problem['rate'],
            link_text_str.format( SOLUTION_FILENAME, problem['github_url'])
        ]
        print(row_join.join(row_contents))
    return None


##########
# File names
##########

def print_file_names(problem_dicts: list) -> None:
    """Prints the file names for all problems in the directory."""
    for problem in problem_dicts:
        print(problem['file_name'])


def create_file_names(problem_dicts: list) -> None:
    """Creates files for all problems in the directory."""
    pass


##########
# Main
##########

def main():
    driver = get_driver()
    elements = get_elements(driver, PROBLEM_CLASS, LOCATE_BY)

    problem_dicts = get_problem_info(elements)
    create_md_row(problem_dicts)


if __name__ == "__main__":
    main()

