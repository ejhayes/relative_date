#!/usr/bin/env python

"""
Tests NumberList and FrequencyDistribution, classes for statistics.
"""

from unittest import TestCase
from lib.relative import *
from random import randrange

# Constants to be used throughout testing
minuteDescriptions = "minutes,minute,min,mins,m".split(",")
befores = "in".split(",")
afters = "ago".split(",")
separators = [" ",""]


def fmt(dt):
    # if we count milliseconds the tests may fail on some systems
    return datetime.strftime(dt, "%m/%d/%Y %H:%M:%S")

class relativeDateTests(TestCase): 

    

    def setUp(self):
        self.r = relativeDate()
        
    def test_now(self):
        """should be the current time"""
        self.assertEqual(fmt(datetime.now()),fmt(self.r.parse("now")))
        
    def test_positive_mins(self):
        # run various tests for minutes
        mins = randrange(0,60)

        
        for minuteDescription in minuteDescriptions:
            for sep in self.separators:
                s = "in %d%s%s" % (mins, sep, minuteDescription)
                
                self.assertEqual(
                    fmt(datetime.now() + timedelta(minutes=mins)), 
                    fmt(self.r.parse(s)),
                    s
                )
        
    def test_negative_mins(self):
        mins = randrange(0,60)