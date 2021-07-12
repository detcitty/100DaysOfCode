# https://www.codewars.com/kata/52fefe6cb0091856db00030e/train/python

from datetime import datetime
"""
1 byte = 9 bits
a 4-byte timestamp value, representing the ObjectId's creation, measured in seconds since the Unix epoch
a 5-byte random value
a 3-byte incrementing counter, initialized to a random value
"""

class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        pass
    
    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        pass