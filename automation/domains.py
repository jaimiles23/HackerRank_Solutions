"""
Creates Domain classes for the automation scripts.

The domain classes help navigate between directories in each challenge domain.
"""

##########
# Imports
##########

from dataclasses import dataclass
from logger import logging


##########
# Domains
##########
"""
Domains has 3 sections:
    1. Define the domain class
    2. Set the domain information
    3. Create the domain classes.
"""

##### Define Domain Class
@dataclass
class DomainInfo(object):
    """Class for tracking soution Domains & urls"""
    number: int
    info: dict

    def __post_init__(self):
        # Name
        logging.debug(f"Creating {self.info['name']} class")
        self.name = self.info.pop('name')
        self.filetype = self.info.pop('filetype')



##### Domain Information
sql = {
    'name'                  :   'sql',
    'filetype'              :   'sql',
    'Basic Select'          :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=select',
    'Advanced Select'       :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=advanced-select',
    'Aggregation'           :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=aggregation',
    'Basic Join'            :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=join',
    'Advanced Join'         :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=advanced-join',
    'Alternative Queries'   :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=alternative-queries',
}

stats = {
    'name'      :   'statistics',
    'filetype'  :   'ipynb',        
    '10_days'   :   'https://www.hackerrank.com/domains/tutorials/10-days-of-statistics'
}


##### Create Domain Classes
domain_list = [
    sql,
    stats
]

problem_domains = []
for i in range(len(domain_list)):
    problem_domains.append(DomainInfo(i, domain_list[i]))