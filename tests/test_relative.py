#!/usr/bin/env python

'''
Tests NumberList and FrequencyDistribution, classes for statistics.
'''

from lib.relative import *
from random import randrange
from nose.tools import *
from nose.exc import SkipTest
eq=eq_

# Constants to be used throughout testing
abbr_mins = 'minutes,minute,min,mins,m'.split(',')
abbr_hours = 'hours,hour,hr,h,hrs'.split(',')
abbr_days = 'days,day,d,'.split(',')
abbr_incr = '+,'.split(',')
abbr_befores = 'in'.split(',')
abbr_afters = 'ago'.split(',')
separators = [' ','']

def fmt(dt):
    # if we count milliseconds the tests may fail on some systems
    return datetime.strftime(dt, '%m/%d/%Y %H:%M:%S')

def time_permutation(abbr_time, duration):
    if(duration >= 0):
        # to happen in the future
        for before in abbr_befores:
            for t in abbr_time:
                for sep in separators:
                    yield '%s %s%s%s' % (before,duration,sep,t)
        
        # issued with an incrementer
        for inc in abbr_incr:
            for t in abbr_time:
                for sep in separators:
                    yield '%s%s%s%s' % (inc,duration,sep,t)
                    
    else:
        # happened in the past
        for after in abbr_afters:
            for t in abbr_time:
                for sep in separators:
                    yield '%s%s%s %s' % (duration * -1,sep,t,after)
        
        # issued with a decrementer
        for t in abbr_time:
            for sep in separators:
                yield '%s%s%s' % (duration,sep,t)
                    
class test_relative(): 

    def setUp(self):
        self.r = relativeDate()
        
    def test_now(self):
        '''should be the current time'''
        eq(fmt(datetime.now()),fmt(self.r.parse('now')))

    def compare_time(self,s,delta):
        eq(fmt(datetime.now()+delta), fmt(self.r.parse(s)))
        
    def test_min_permutations(self):        
        # future permutations
        durationTests = [0,1,randrange(2,59),60]
        
        for duration in durationTests + [-1*i for i in durationTests]:
            for i in time_permutation(abbr_mins,duration):
                yield self.compare_time, i, timedelta(minutes=duration)
                
    def test_hour_permutations(self):        
        # future permutations
        durationTests = [0,1,randrange(2,23),24]
        
        for duration in durationTests + [-1*i for i in durationTests]:
            for i in time_permutation(abbr_hours,duration):
                yield self.compare_time, i, timedelta(hours=duration)
        
    def test_day_permutations(self):        
        # future permutations
        durationTests = [0,1,randrange(2,30),31]
        
        for duration in durationTests + [-1*i for i in durationTests]:
            for i in time_permutation(abbr_days,duration):
                yield self.compare_time, i, timedelta(days=duration)
    
        
# run comparisons on the various permutations
