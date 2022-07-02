# !/usr/bin/env bash
# coding=utf-8

# Time

import time

# get time stamp
# only time between 1970 and 2038
ticks = time.time()
print('Current time stamp is ', ticks);

# get current time
localtime = time.localtime(time.time())
print('Local time is ', localtime)

# get format time
localtime = time.asctime(localtime)
print('Local time is ', localtime)

# format date
print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
# date to time stamp
a = 'Sat Mar 28 22:23:35 2022'
print(time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')))


# Calender
import calendar

cal = calendar.month(2022, 5)
print(cal)

