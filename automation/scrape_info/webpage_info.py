"""
Open firefox driver and scape WebPageInfo.
"""

##########
# Imports
##########

import time
from typing import Tuple

import constants
from logger.scrape_info import logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

##########
# Driver
##########

class WebPageInfo():

    filename_accountinfo = constants.HR_ACCOUNT_INFO_FILENAME
    login_url = constants.HR_LOGIN_URL
    ## XML path to login button
    loginbutton_xml = constants.SEL_LOGIN_BUTTON_XML
    

    ## Selenium Class identifiers
    LOCATE_BY = constants.SEL_LOCATE_BY
    CHALLENGE_CLASSNAME = constants.SEL_CHALLENGE_CLASSNAME
    
    
    ##### Driver methods
    @classmethod
    def start_driver(cls) -> object:
        """Returns Firefox driver object.

        NOTE: If running the remote driver, need to create standalone server. 
        Run the following command on cmd
            >>> java -jar selenium-server-standalone-3.141.0.jar -port 4446

        ## Remote server
        # driver = webdriver.Remote(
        #     command_executor='http://127.0.0.1:4446/wd/hub',
        #     desired_capabilities=DesiredCapabilities.FIREFOX)
        """
        logging.debug("WebPageInfo: Opening Driver.")
        cls.driver = WebPageInfo.login_hackerrank(webdriver.Firefox())

    
    @staticmethod
    def login_hackerrank(driver: object) -> object:
        """Returns driver after login to hackerrank.com.
        """
        logging.debug("WebPageInfo - logging into Hackerrrank.")
        driver.get( WebPageInfo.login_url)
        account_name, account_pw = WebPageInfo.read_account_info()
        
        driver.find_element_by_id('input-1').send_keys(account_name)    ## Username
        driver.find_element_by_id('input-2').send_keys(account_pw)      ## Password
        driver.find_element_by_class_name('checkbox-input').click()     ## Remember
        driver.find_element_by_xpath(WebPageInfo.loginbutton_xml).click()   ## Login button
        time.sleep(0.5)
        return driver
    

    @staticmethod
    def read_account_info() -> Tuple[str, str]:
        """Returns Tuple representing email & account password.

        Returns:
            Tuple[str, str]: Email & password
        """
        logging.debug("WebPageInfo - reading account information.")
        with open(WebPageInfo.filename_accountinfo) as infile:
            return infile.readlines()


    ##### Init
    def __init__(self, url: str, scrape: bool = True):
        """Init webbpage object
        """
        logging.debug(f"WebPageInfo - opening {url}")
        self.url = url
        self.open_url()
        if scrape:
            self.challenge_info = self.get_challenge_info()
    

    ##### WebPageInfo methods
    def open_url(self) -> "driver":
        """Opens URL on class driver.
        """
        self.driver.get(self.url)
        for _ in range(10):
            self.scroll_to_bottom()
            time.sleep(0.1)
        return

    
    def scroll_to_bottom(self) -> None:
        """Scrolls to bottom of driver WebPageInfo.
        """
        for _ in range(3):
            time.sleep(0.01)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return


    ##### Scrape information
    def get_challenge_info(self) -> list:
        """Gets all challenge problem information from the URLs"""
        logging.debug("WebPageInfo - getting challenge info.")
        if WebPageInfo.LOCATE_BY == "class":
            challenge_info = WebPageInfo.driver.find_elements_by_class_name(WebPageInfo.CHALLENGE_CLASSNAME)
        else:
            raise Exception("Must indicate how to locate HTML elements.")

        if len(challenge_info):
            return challenge_info
        raise Exception("Could not locate elements!")


