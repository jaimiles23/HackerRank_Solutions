
##########
# Imports
##########
import logging

##########
# is challenge
##########

def is_challenge(challenge: object) -> (bool, str):
    """Returns boolean indicating if scraped info is challenge.

    Args:
        challenge (object): Scraped webinfo

    Returns:
        bool: If is challenge.
    """
    ## Check can convert
    try: 
        text = challenge.text
    except Exception as E:
        logging.error(f"Exception: {E}")
        return (False, None)
    
    ## Check advert
    adverts = (
        "HackerRank Skills Certification Test",
        )
    for a in adverts:
        if a in text:
            logging.debug(f"ADVERT - Found {a} in text")
            return (False, None)
    return True, text
