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

DOMAIN = 'domain'
FILETYPE = 'filetype'


##### Define Domain Class
@dataclass
class DomainInfo(object):
    """Class for tracking soution Domains & urls"""
    number: int
    info: dict

    def __post_init__(self):
        # Name
        logging.debug(f"Creating {self.info[DOMAIN]} class")
        setattr(self, DOMAIN, self.info.pop(DOMAIN))
        setattr(self, FILETYPE, self.info.pop(FILETYPE))


##### Domain Information
sql = {
    DOMAIN                  :   'sql',
    FILETYPE                :   'sql',
    'Basic Select'          :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=select',
    'Advanced Select'       :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=advanced-select',
    'Aggregation'           :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=aggregation',
    'Basic Join'            :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=join',
    'Advanced Join'         :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=advanced-join',
    'Alternative Queries'   :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=alternative-queries',
}

stats = {
    DOMAIN      :   'statistics',
    FILETYPE    :   'ipynb',        
    '10_days'   :   'https://www.hackerrank.com/domains/tutorials/10-days-of-statistics'
}


##### Create Domain Classes
domains = [
    sql,
    stats
]

for i in range(len(domains)):
    domains[i] = DomainInfo(i, domains[i])