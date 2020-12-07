"""
Creates Domain classes for the automation scripts.

The domain classes help navigate between directories in each challenge domain.
To include a new domain, createa a domain dictionary with the following keys:
- name: used for overall domain
- filetype: extension to use on files
- subdomain & relevant url (key, value) pair: subdomain name & url to scrape.

Then, add the domain to the domain_list. e.g.,

```python3
## Sample Domain
sql = {
    'name'                  :   'sql',
    'filetype'              :   'sql',
    'Basic Select'          :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=select',
    'Advanced Select'       :   'https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=advanced-select'
   }
```
"""

##########
# Imports
##########

from dataclasses import dataclass

from logger.scrape_info import logging


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
        logging.debug(f"Creating {self.info['name']} DomainInfo")
        self.name = self.info.pop('name')
        self.filetype = self.info.pop('filetype')
        self.total_url = self.info.pop('total_url')


##### Domain Information
sql = {
    'name'                  :   'sql',
    'filetype'              :   'sql',
    'total_url'             :   'https://www.hackerrank.com/domains/sql',
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
    'total_url' :   'https://www.hackerrank.com/domains/tutorials/10-days-of-statistics',
    '10_days'   :   'https://www.hackerrank.com/domains/tutorials/10-days-of-statistics'
}

databases = {
    'name'                      :   'databases',
    'filetype'                  :   'md',
    'total_url'                 :   'https://www.hackerrank.com/domains/databases',
    'Relational Algebra'        :   'https://www.hackerrank.com/domains/databases?filters%5Bsubdomains%5D%5B%5D=relational-algebra',
    'Indexes'                   :   'https://www.hackerrank.com/domains/databases?filters%5Bsubdomains%5D%5B%5D=indexes',
    'OLAP'                      :   'https://www.hackerrank.com/domains/databases?filters%5Bsubdomains%5D%5B%5D=olap',
    'Set and Algebra'           :   'https://www.hackerrank.com/domains/databases?filters%5Bsubdomains%5D%5B%5D=set-and-algebra',
    'NoSQL - XML, MapReduce'    :   'https://www.hackerrank.com/domains/databases?filters%5Bsubdomains%5D%5B%5D=xpath-queries',
    'Database Normalization'    :   'https://www.hackerrank.com/domains/databases?filters%5Bsubdomains%5D%5B%5D=database-normalization',
}

python = {
    'name'  :   'python',
    'filetype'      :   'py',
    'total_url'     :   'https://www.hackerrank.com/domains/python',
    'introduction'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction',
    'Basic Data Types'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-basic-data-types',
    'Strings'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-strings',
    'Sets'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-sets',
    'Math'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-math',
    'Itertools'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-itertools',
    'Collections'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-collections',
    'Date and Time'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-date-time',
    'Errors and Exceptions'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=errors-exceptions',
    'Classes'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-classes',
    'Built-Ins'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-built-ins',
    'Python Functionals'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-functionals',
    'Regex and Parsing'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-regex',
    'XML'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=xml',
    'Closures and Decorators'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=closures-and-decorators',
    'Numpy'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=numpy',
    'Debugging'  :   'https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-debugging',
}


##### Create Domain Classes
domain_list = (
    # sql,
    # stats,
    databases,
    # python,
)

problem_domains = []
for i in range(len(domain_list)):
    problem_domains.append(DomainInfo(i, domain_list[i]))
