"""
Contains constants for the automation module.
"""

##########
# Domains
##########

# TODO: create data class with name for domain, and then dict of subdirs & urls to fill those subdirs?
# can also include things like problem count in domain?
# & method to change to that subdir?



##########
# Tables
##########
TBL_COLNAMES = (
    'Number', 
    'Challenge', 
    'Score', 
    'Difficulty', 
    'Rate', 
    'Solution',
)


##########
# Table of Contents
##########
TOC_HEADER = "#hackerrank"

## HTML identifiers
PROBLEM_CLASS = 'challengecard-title' # class
PROBLEM_TAG = 'h4'                # tag

## location method
LOCATE_BY = "class"
