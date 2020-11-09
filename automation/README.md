
# Automation

## Purpose
This directory contains automation for my Hacker Rank Solutions. Automation falls into 2 categories:
1. Selecting Practice Challenges, and
2. Updating the README.

I ultimately want scripts to automatically (1) select a random practice challenge for me to complete and (2) update the README.md with my solution.


### Selecting Practice Challenges
I am currently designing a script to randomly select practice challenges for me to solve. This script will allow for additional parameters to accomodate:
- Challenge domains: e.g., Python, SQL, Statistics
- Challenge type: new or review

This script will have 6 steps:
1. Access the problem domain, either through a passed parameter or randomly selected.
2. Navigate to the relevant directory.
3. Read stored data available challenges.
4. Randomly select challenge to complete.
5. Create file to contain solution.
6. Open challenge URL.


### Updating README
I automatically update the README with challenge information. This includes the challenge's name, url, difficulty, acceptance rate, and link to my solution.

To update the README, I wrote a script with 3 general steps:
1. Connect to the challenge webpage.
2. Extract the challenge's information.
3. Write formatted the formatted information to a table in the README.