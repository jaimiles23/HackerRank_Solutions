"""
Open firefox driver and scape webpage. 
"""

##########
# Imports
##########

import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


##########
# Driver
##########

class WebPage():

    def __init__(self, url: str, locate_by: str, identifier: str):
        self.url, self.locate_by, self.identifier = url, locate_by, identifier
        self.driver = self.open_webdriver()


    def open_webdriver(self) -> "driver":
        """Returns Selenium webdriver with open url page.

        Args:
            url (str): url to open

        Returns:
            "driver": Driver to return.
        
        NOTE: If running the remote driver, need to create standalone server. 
        Run the following command on cmd
            >>> java -jar selenium-server-standalone-3.141.0.jar -port 4446
        """
        ## Desktop
        driver = webdriver.Firefox()

        ## Chrome driver
        # driver = webbrowser.Chrome(r"C:\Users\Jai\chromedriver.exe")  # path to Chromedriver. Need work to get method working.

        ## Remote server
        # driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4446/wd/hub',
        #     desired_capabilities=DesiredCapabilities.FIREFOX)
        
        driver.get(self.url)
        return driver


    def get_info( self) -> list:
        """Auxiliary method to get list of elements with identifier."""

        for _ in range(5):
            time.sleep(20)       # NOTE: Need timer so whole page loads.
            
            if self.locate_by == "class":
                output = self.driver.find_elements_by_class_name(self.identifier)
            elif self.locate_by == "tag":
                output = self.driver.find_elements_by_tag_name(self.identifier)
            else:
                raise Exception("Must indicate how to locate HTML elements.")

            if len(output):
                return output
            
            time.sleep(0.1)     # Table may not load immediately, try 5x
        
        raise Exception("Could not locate elements!")
