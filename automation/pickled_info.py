""" Script to gather pickled information from directories.

Pickled information includes:
- Problem numbers
- Problem URLs
- If the problem is completed or not.
    - Once the problem is marked as complete, the problem will be written to the markdown file.
    NOTE: Should have a warning appear on .bat script that 
"""

##########
# Imports
##########

import pickle

##########
# Pickle Class
##########

class PickleAccesor(object):

    def __init__(self, dir):
        """Initializes the picke filename

        Args:
            dir (str): Pickle name and directory
        """
        self.filename = ''.join([
            'pickle', '_', dir, '.p'
        ])


    def load_problem_urls(self) -> dict:
        """Returns dictionary of problem urls if they have been created yet."""
        try:
            return pickle.load( open(self.filename, 'rb'))
        except (FileNotFoundError):
            return dict()


    def save_problem_urls(self, problem_dicts: list) -> None:
        """Saves pickled object of the problem urls. 

        google.lucky() has a ratelimit and will limit requests. Thus, if problem URL
        has already been acquired, save it in pickled object to avoid repetitive requests.
        """
        problem_url_dict = dict()

        for problem in problem_dicts:
            problem_name, problem_url = problem['name'], problem['problem_url']
            problem_url_dict[problem_name] = problem_url
        
        pickle.dump( problem_url_dict, open(self.filename, 'wb'))
        return None

