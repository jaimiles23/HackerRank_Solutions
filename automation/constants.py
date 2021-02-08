"""
Contains constants for Solution automation 
"""

##########
# INPUT 
##########
INPUT_REVIEW = 'r'

INPUT_CHALL_DOMAIN = {
    'py'    :   'python',
    'sql'   :   'sql',
    'stats' :   'statistics',
    'db'    :   'databases'
}

##########
# CSV
##########

CSV_FILE_NOMENCLATURE = "{}_info.csv"

CHALLENGE_INFO_CSV_HEADERS = (
    'num',
    'name',
    'score',
    'difficulty',
    'rate',
    'url',
    'solution_url',
    'completed',            # Binary. if yes, write to MD.
    'TODO',                 # Binary. if to be solved.
)

##########
# Hackerrank 
##########

HR_LOGIN_URL = 'https://www.hackerrank.com/auth/login'
HR_ACCOUNT_INFO_FILENAME = 'account_info.txt'

## NOTE: Next time, make this a list& iterate over ever element.
SEL_LOGIN_BUTTON_XML = "/html/body[@id='hr_v2']/div[@id='content']/div[@class='ui-kit-root']/div[@class='body-wrap community-page auth-page login-page']/div[@class='show-cookie-banner']/div[@class='theme-m new-design']/div[@class='community-content']/div[@class='auth-container container theme-m']/div[@class='auth-content-wrap']/div[@class='auth-box-container']/div[@class='auth-box']/div[@class='ui-tabs-wrap auth-content']/div[@id='tab-1-content-1']/div[@class='login-form auth-form theme-m']/form[@class='form']/div[@class='form-item clearfix']/button[@class='ui-btn ui-btn-large ui-btn-primary auth-button ui-btn-styled']/div[@class='ui-content align-icon-right']/span[@class='ui-text']"
SEL_LOGIN_HTML_CLASS = "ui-btn ui-btn-large ui-btn-primary auth-button ui-btn-styled"

SEL_LOCATE_BY = "class"
SEL_CHALLENGE_CLASSNAME = 'challengecard-title'

FULLSCREEN_URL = "?isFullScreen=true"

##########
# GitHub 
##########
GH_USERNAME = 'jaimiles23'
GH_REPO_NAME = "HackerRank_Solutions"
GH_SOL_URL = f"https://github.com/{GH_USERNAME}/{GH_REPO_NAME}" + "/blob/master/{}/{}/{}"


##########
# Readme 
##########

########## Challenge Table

CHALL_TBL_COLNAMES = (
    'Number', 
    'Challenge', 
    'Score', 
    'Difficulty', 
    'Rate', 
    'Solution',
)

########## Files

TOC_HEADER = "#hackerrank"

PRE_README_FILENAME = "pre_README.md"
README_FILENAME = "README.md"
README_CONTENTS_FILENAME = "readme_contents.md"
TOC_FILENAME = "toc_readme.md"

LINE_BREAK = "\n<br/>\n"


########## NB VIEWER
NB_VIEWER_SOL_TEXT = "nbviewer"
COL_NB_VIEWER = "Solution 2"
NB_VIEWER_URL = "https://nbviewer.jupyter.org/"

NB_DOMAINS = (
    "statistics",
)

########## Table of Contents

TOC_UPPER_DIRS = (
    'SQL',
    'OLAP',
)

TOC_NUM_DIRS = (
    "10_days",
)