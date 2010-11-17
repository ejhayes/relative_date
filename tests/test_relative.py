#!/usr/bin/env python

'''
Tests NumberList and FrequencyDistribution, classes for statistics.
'''

from unittest import TestCase
from lib.relative import *
from random import randrange
from nose.tools import *

# Constants to be used throughout testing
abbr_mins = 'minutes,minute,min,mins,m'.split(',')
abbr_hours = 'hours,hour,hr,h,hrs'.split(',')
abbr_days = 'days,day,d'.split(',')
abbr_incr = '+'.split(',')
abbr_befores = 'in'.split(',')
abbr_afters = 'ago'.split(',')
separators = [' ','']

def fmt(dt):
    # if we count milliseconds the tests may fail on some systems
    return datetime.strftime(dt, '%m/%d/%Y %H:%M:%S')

class relativeDateTests(TestCase): 

    def setUp(self):
        self.r = relativeDate()
        
    def test_now(self):
        '''should be the current time'''
        self.assertEqual(fmt(datetime.now()),fmt(self.r.parse('now')))
        
    def test_negative_mins(self):
        mins = randrange(0,60)
        
# run comparisons on the various permutations
def test_min_permutations(abbr_time=abbr_mins,timeDeltaParam='minutes',upTo=60):
    r = relativeDate()
    
    # future permutations
    for before in abbr_befores:
        for t in abbr_time:
            for sep in separators:
                for i in range(upTo):
                    s = '%s %s%s%s' % (before,sep,i,t)
                    
                    yield compare_time, r, s, timedelta(**{timeDeltaParam:i})
                    
    # past permutations
    for after in abbr_afters:
        for t in abbr_time:
            for sep in separators:
                for i in range(upTo):
                    s = '%s%s%s %s' % (sep,i,t,after)

                    yield compare_time, r, s, timedelta(**{timeDeltaParam:i*-1})

def test_hour_permutations(abbr_time=abbr_hours,timeDeltaParam='hours',upTo=24):
    r = relativeDate()

    # future permutations
    for before in abbr_befores:
        for t in abbr_time:
            for sep in separators:
                for i in range(upTo):
                    s = '%s %s%s%s' % (before,sep,i,t)

                    yield compare_time, r, s, timedelta(**{timeDeltaParam:i})
                    
    # past permutations
    for after in abbr_afters:
        for t in abbr_time:
            for sep in separators:
                for i in range(upTo):
                    s = '%s%s%s %s' % (sep,i,t,after)

                    yield compare_time, r, s, timedelta(**{timeDeltaParam:i*-1})
    
    
def test_day_permutations(abbr_time=abbr_days,timeDeltaParam='days',upTo=28):
    r = relativeDate()

    # future permutations
    for before in abbr_befores:
        for t in abbr_time:
            for sep in separators:
                for i in range(upTo):
                    s = '%s %s%s%s' % (before,sep,i,t)

                    yield compare_time, r, s, timedelta(**{timeDeltaParam:i})
                    
    # past permutations
    for after in abbr_afters:
        for t in abbr_time:
            for sep in separators:
                for i in range(upTo):
                    s = '%s%s%s %s' % (sep,i,t,after)

                    yield compare_time, r, s, timedelta(**{timeDeltaParam:i*-1})
                    
def compare_time(r,s,delta):
    assert fmt(datetime.now()+delta) == fmt(r.parse(s))