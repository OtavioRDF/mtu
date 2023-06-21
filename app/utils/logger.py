import logging

# create logger
logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)

# create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# adding formatter to console handler
console_handler.setFormatter(formatter)

# adding console handler to logger 
logger.addHandler(console_handler)