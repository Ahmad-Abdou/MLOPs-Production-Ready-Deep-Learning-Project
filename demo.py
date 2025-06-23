import sys
from us_visa.logger import logging

from us_visa.exception import USvisaException


# logging.info("Weclome to our custome log.")

try:
    a = 1 / 0  
except Exception as e:
    raise USvisaException(e, sys) from e