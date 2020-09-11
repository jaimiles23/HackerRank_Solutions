"""/**
 * @author [Jai Miles]
 * @email [jaimiles23@gmail.com]
 * @create date 2020-09-06 12:31:54
 * @modify date 2020-09-06 17:21:02
 * @desc [
    Script to webscrape hackerrank problems and format them into README.md markdown table.

    Code Sections:
    1. Constants
        - used for web scraping and dirs
    2. Imports
    3. Driver
        - Instantiate Selenium driver
        - get_elements method to retrieve html
    4. Get Info 
        - gets/constructs information about each challenge
    5. Pickled Problem URLS
        - pickels challenge URLs to avoid HTTP 429 rate limits on google webscraping
    6. Print Markdown Table
        - prints entire table to be pasted into README.md
    7. Challenge Files
        - creates non-existent files 
        - prints file names

    Usage:
    - Change HACKERRANK_WEBPAGE and run
    - print_md_tables() prints rows to paste into README.md for that section
    - print_file_names() used to view filename format
    - create_files() creates files from filenames

   ]
 */
"""

##########
# Constants
##########
"""
This section changes constants processed by the script.

Change 3 constants b/w runs:
- hackerrank_webpage - correct filter to create table
- lang_dir - language practicing
- sub_dir - directory to store code into
"""

## URL - change subdomain filter per problem
GITHUB_URL_BASE = "https://github.com/jaimiles23/HackerRank_Solutions/blob/master/{}/{}/{}"
HACKERRANK_WEBPAGE = "https://www.hackerrank.com/domains/tutorials/10-days-of-statistics"
# NOTE: Some learning challenges require your profile to access
# Easy solution here is to log-in with webbrowser with github profile
# Sufficient time allowed to log-in.


## Dirs/filenames for repo
LANG_DIR = "statistics"
SUB_DIR = "10_days"
PICKLE_DIR = "pickle\\"
SOLUTION_FILENAME = "MySQL"

## Table headers
columns = ('Number', 'Challenge', 'Score', 'Difficulty', 'Rate', 'Solution')

## Create back to TOC Header
TOC_HEADER = "#hackerrank"

## HTML identifiers
PROBLEM_CLASS = 'challengecard-title' # class
PROBLEM_TAG = 'h4'                # tag

## location method
LOCATE_BY = "class"


##########
# Imports
##########

import os
import pickle
import sys
import time
import webbrowser
from typing import List

import bs4
import googlesearch
import requests
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

    ## Chrome driver
    # driver = webbrowser.Chrome(r"C:\Users\Jai\chromedriver.exe")  # path to Chromedriver. get method not workign

    ## Remote server
    # driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4446/wd/hub',
    #     desired_capabilities=DesiredCapabilities.FIREFOX)
    
    driver.get(HACKERRANK_WEBPAGE)
    return driver


def get_elements( driver: object, identifier: str, LOCATE_BY: str) -> list:
    """Auxiliary method to get list of elements with identifier."""

    for _ in range(5):
        time.sleep(20)       # NOTE: Need timer so whole page loads.
        
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
        def remove_special_chars(file_name: str) -> str:
            """Aux func to remove special characters from file name."""
            special_chars = ['<', '>', ':', '"', "'", '/', '\\', '|', '?', '*']
            for char in special_chars:
                file_name = file_name.replace(char, '_')
            return file_name


        num_problems, problem_num = str(num_problems), str(problem_num)
        while len(num_problems) != len(problem_num):
            problem_num = '0' + problem_num
        
        file_name = ''.join([
            problem_num,
            "_",
            name.replace(' ', '_').lower(),
            ".sql"
        ])

        return remove_special_chars(file_name)
    

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
    

    def _get_problem_url(problem_name: str, problem_url_dict: dict) -> str:
        """Returns url of challenge problem from text.
        
        NOTE: Some URLS do not follow the specified format. e.g.
            https://www.hackerrank.com/challenges/salary-of-employees for Employee Salaries problem.
                url_base = "https://www.hackerrank.com/challenges/{}/problem"
                name = problem_name.replace(" ", "-")
                return url_base.format(name)

        Instead, I used 3rd party library googlesearch. This is much slower
        NOTE:  HTTPError 429 - Too Many Requests
            > Google uses a rate limiter to stop spamming. Does not specify length of timeout.
        """
        if problem_name in problem_url_dict.keys():
            return problem_url_dict[problem_name]
        
        time.sleep(1/5)     # slow HTTP requests
        search_items = "site: hackerrank.com Challenges {}".format(problem_name)
        return (
            googlesearch.lucky(search_items)
                .replace("/forum", "/problem")          # top search may return forum for problem.
        ) 
    

    def _get_github_url(file_name: str) -> str:
        """Returns url of github solution from text."""
        
        return GITHUB_URL_BASE.format( LANG_DIR, SUB_DIR, file_name)


    ########## Create list of dictionaries
    problem_dicts = list()
    problem_num = 0

    ## General vars
    num_problems = len(problems)
    problem_url_dict = load_problem_urls()

    for p in problems:
        ## vars for dict
        text = p.text
        problem_num += 1
        problem_dict = dict()

        ## vars for functions
        problem_name = _get_name(text)
        file_name = _get_file_name(num_problems, problem_num, problem_name)

        ## create dict
        problem_dict = {
            'num'           :   str(problem_num),
            'name'          :   problem_name,
            'file_name'     :   file_name,
            'difficulty'    :   _get_difficulty(text),
            'score'         :   _get_score(text),
            'rate'          :   _get_rate(text),
            'problem_url'   :   _get_problem_url(problem_name, problem_url_dict),
            'github_url'    :   _get_github_url(file_name),
        }
        problem_dicts.append(problem_dict)
    
    return problem_dicts


##########
# Pickled Problem URLs
##########

def get_pickle_file_name() -> str:
    """Returns file name for pickled information."""
    return ''.join([
        PICKLE_DIR,
        LANG_DIR, 
        '_', 
        SUB_DIR, 
        '.p'
    ])


def save_problem_urls(problem_dicts: list) -> None:
    """Saves pickled object of the problem urls. 

    google.lucky() has a ratelimit and will limit requests. Thus, if problem URL
    has already been acquired, save it in pickled object to avoid repetitive requests.
    """
    problem_url_dict = dict()

    for problem in problem_dicts:
        problem_name, problem_url = problem['name'], problem['problem_url']
        problem_url_dict[problem_name] = problem_url
    
    p_filename = get_pickle_file_name()
    pickle.dump( problem_url_dict, open(p_filename, 'wb'))
    return None


def load_problem_urls() -> dict:
    """Returns dictionary of problem urls if they have been created yet."""
    p_filename = get_pickle_file_name()
    try:
        return pickle.load( open(p_filename, 'rb'))
    except (FileNotFoundError):
        return dict()


##########
# Print Markdown Table
##########

def print_md_table(problem_dicts: list) -> None:
    """Prints rows for hacker_rank README.md markdown table for the specified problems.
    
    Markdown table headers as follow:
    Number    |   Challenge   |   Score   |   Difficulty  |   Rate    |   Solution
    """
    star_str = ":star:"
    num_stars = {
        'Easy'      :   1,
        'Medium'    :   2, 
        'Hard'      :   3,
    }
    link_text_str = "[{}]({})"

    print_output_header("print table")

    ## Print table headers
    
    tbl_formatters = [':--' for col in columns]
    for i in [0, 2]:
        tbl_formatters[i] = "--:"       # right align
    print(' | '.join(columns))
    print(' | '.join(tbl_formatters))

    ## Print table rows
    try:
        for problem in problem_dicts:
                row_join = " | "
                row_contents = [
                    problem['num'],
                    link_text_str.format( problem['name'], problem['problem_url']),
                    problem['score'],
                    star_str * num_stars[ problem['difficulty']],
                    problem['rate'],
                    link_text_str.format( SOLUTION_FILENAME, problem['github_url'])
                ]
                print(row_join.join(row_contents))
    except (KeyError):
        for problem in problem_dicts:
            print(problem)
            # for k, v in problem:
                # print(k, "\t", v)

    print_back_to_toc()
    return None


##########
# Challenge Files
##########

def print_file_names(problem_dicts: list) -> None:
    """Prints the file names for all problems in the directory."""
    print_output_header("printing file names")
    for problem in problem_dicts:
        print(problem['file_name'])


def create_files(problem_dicts: list) -> None:
    """Creates files for all problems in the directory.
    
    Checks if the file exists first. If doesn't exist, then creates file
    and adds comments for problem name and fiel requests.
    """
    ## change to appropriate directory
    go_to_dir()

    print_output_header("creating files")
    ## Check for file in each problem & create
    for problem in problem_dicts:
        file_name = problem['file_name']

        if os.path.exists( file_name):
            continue
        
        with open( file_name, 'w') as outfile:
            outfile.write(f"""Solution to: {problem['name']}\n\t\t{problem['problem_url']}""")

        print(f"Created {file_name}")
    

def go_to_dir() -> None:
    """ Changes cwd to desired directory.

    If doesn't exist, creates.
    """
    ## Nested directories
    dirs = [LANG_DIR, SUB_DIR]

    for i in range(1, len(dirs) + 1):
        ## Create path for nested directory.
        path = '\\'.join(dirs[:i])
        if not os.path.exists(path):
            os.mkdir(path)

    os.chdir(path)


##########
# Auxiliary Methods
##########
def print_output_header(header: str) -> None:
    """Prints header for output."""
    line = "\n" + "#" * 15 + "\n"
    print(line, SUB_DIR, header.upper(), line,
        sep = " ", end = "\n\n")


def print_back_to_toc() -> None:
    """Prints method to return to TOC."""
    print("""
<br/>
<div align="right">
    <b><a href="{}">⬆️ To Top</a></b>
</div>
<br/>
""".format(TOC_HEADER))


##########
# Main
##########

def main():
    driver = get_driver()
    elements = get_elements(driver, PROBLEM_CLASS, LOCATE_BY)

    problem_dicts = get_problem_info(elements)
    save_problem_urls(problem_dicts)

    ## Print file names
    # print_file_names(problem_dicts)

    ## Create files
    create_files(problem_dicts)

    ## Markdown rows
    print_md_table(problem_dicts)


if __name__ == "__main__":
    main()

