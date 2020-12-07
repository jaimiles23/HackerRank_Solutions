import os
import logging

logging.basicConfig(
    filename = os.path.dirname(os.path.realpath(__file__)) +  'log_select_chall.txt', 
    filemode= 'w', 
    level=logging.DEBUG,
    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s', 
    )