
# Automation

## Purpose
This directory contains automation for my Hacker Rank Solutions. Automation falls into 2 categories:
1. Select Challenge
2. Update Readme


### Select Challenge
I am currently designing this script to randomly select practice challenges for me to solve. This script will allow for additional parameters to accomodate:
- Challenge domains: e.g.,  SQL, Statistics
- Challenge type: new or review
- Challenge order: complete the next challenge in the series

This script will have 6 steps:
1. Access the problem domain
2. Navigate to the relevant directory
3. Read stored data on the available challenges
4. Randomly select challenge to complete
5. Create file to contain solution
6. Open challenge URL


### Update README
I automatically update the README tables with challenge information. This includes the challenge's name, url, difficulty, acceptance rate, and link to my solution.

The script to update the README has 3 steps:
1. Open and scrape webpage
2. Parse HTML for problem information
3. Write information to a formatted table in the README

