#!/usr/bin/python3
""" 
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys
import re


def read_line():
    """ Reads the lines from stdin"""
    line = ""

    for i in sys.stdin.readline():
        line += i
    return line


count = 1
status_dicts = {}
while True:
    log_line = read_line()
    pattern = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(?P<date>[^\]]+)\] "GET /projects/260 HTTP/1.1" (?P<status>\d{3}) (?P<size>\d+)'
    match = re.match(pattern, log_line)
    if match:
        ip = match.group('status')
        size = match.group("size")
        if ip in status_dicts.keys():
            status_dicts[ip] += 1
        else:
            status_dicts[ip] = 1
        if count % 10 == 0:
            print(f"File size: {size}")
            for key in sorted(status_dicts.keys()):
                print(f"{key}: {status_dicts[key]}")
    count += 1
