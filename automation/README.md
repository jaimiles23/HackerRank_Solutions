
# Automation

## Purpose
This directory contains automation for my Hacker Rank Solutions. There are 3 automation methods:
1. _scrape_info
1. _write_to_md
1. _start_challenge

NOTE: The _start_challenge script may be run via the `hr_chall.bat` script in the `bat_scripts` folder.


### _scrape_info
This script scrapes hackerrank challenge information and saves it the repository directory. The script connects to the domain and sub-domain urls listed in `domains.py`. It web scapes challenges information with Selenium, saves the information to a csv, and creates solution files. Updates are automatically pushed to the portfolio with the "init" method.

### _write_to_md
This script writes challenge information to markdown files for this repository. It reads challenge information from csvs and checks if the challenges are complete. If the challenge is complete, the script writes the challenges to a markdown table in the subdomain README.md file. Sub-domain README.md files are written to the Domain README.md file, which are subsequently written to the master README.md file. 

### _start_challenge
This script selects a challenge to complete. The script recursively navigates through domains and sub-directories and reads the challenge information csvs to locate a challenge that is marked `TODO` and not `Completed`. Once it locates a challenge, it opens the challenge in the webbrowser and in system process to complete. The script asks the user if the challenge has been completed. If not, it asks the user if the challenge should remain on the TODO list. If the challenge is completed or removed from the TODO list, the change is pushed to the github repo.
