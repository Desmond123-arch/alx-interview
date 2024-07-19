#!/usr/bin/python3

"""
reads stdin line by line and computes metrics
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
    pattern = (
        r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
        r'\[(?P<date>[^\]]+)\] '
        r'"GET /projects/260 HTTP/1.1" '
        r'(?P<status>\d{3}) '
        r'(?P<size>\d+)'
    )

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
