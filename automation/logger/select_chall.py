import logging

logging.basicConfig(
    filename = 'log_select_chall.txt', 
    filemode= 'w', 
    level=logging.DEBUG,
    format = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s', 
    )