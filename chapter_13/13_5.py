"""
Render a calendar

Write a program that takes a set of events, and determines the maximum number of events that can happen concurrently

I.E. find the overlap

I.e. the max number of overlapping intervals

Are the intervals sorted?
Sorted by start time, tie breaker by middle 
What about end time?

Basic idea: sort the list array by start time

As long as you check the longest events first, you don’t have to check the remaining equal start times


|——————|
                   |——| 
|——|
| ———— |

Basic idea:
for each event, count the start times that are inside it’s end time
Keep track of the max
"""

import collections


Interval = collections.namedtuple('Interval', ('start', 'end'))
Event = collections.namedtuple('Event', ('start', 'end'))


def find_max_concurrent_events(events):

    max_so_far = float('-inf')
    interval = Interval(0,0)
    events.sort(key=lambda e: e.end - e.start, reverse=True) # first sort to make sure larger intervals are first
    print(events)
    events.sort(key=lambda e: e.start) #then sort to make sure that we start with earliest times
    i = 0
    print(events)
    while i < len(events):
        while i < len(events) and events[i].end <= interval.end:  #the next interval to check should end after the last interval
            i += 1
        if i >= len(events):
            break
        interval = Interval(events[i].start, events[i].end)
        max_so_far = max(find_interval_max(events, interval, i), max_so_far) #find the max overall for the interval
        i += 1
        while i < len(events) and interval.start == events[i].start: #we can skip events that start at the same time as the last interval
            i += 1
    return max_so_far

def find_interval_max(events, interval, i):
    interval_max = 0
    print(interval)
    prev_event = events[i]
    while i < len(events) and events[i].start < interval.end:
        if prev_event.end < events[i].start:
            interval_max -= 1
        print(events[i])
        interval_max += 1
        prev_event = events[i]
        i += 1
        
    print(interval_max)
    return interval_max

if __name__ == '__main__':
    events = [Event(1,5),Event(2,7),Event(4,5),Event(6,10),Event(8,9),Event(9,17),Event(11,13),
        Event(12,15),Event(14,15)]
    print(find_max_concurrent_events(events))