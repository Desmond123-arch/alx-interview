#!/usr/bin/python3

"""
reads stdin line by line and computes metrics
"""
import sys
import re


def read_line():
    """Reads a line from stdin"""
    return sys.stdin.readline()


count = 1
total_size = 0
status_dicts = {}

try:
    while True:
        log_line = read_line()
        if not log_line:
            break
        pattern = (
            r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - '
            r'\[(?P<date>[^\]]+)\] '
            r'"GET /projects/260 HTTP/1.1" '
            r'(?P<status>\d{3}) '
            r'(?P<size>\d+)'
        )
        match = re.match(pattern, log_line)
        if match:
            status = match.group('status')
            size = int(match.group("size"))
            total_size += size
            if status in status_dicts:
                status_dicts[status] += 1
            else:
                status_dicts[status] = 1
            if count % 10 == 0:
                print(f"File size: {total_size}")
                for key in sorted(status_dicts.keys()):
                    print(f"{key}: {status_dicts[key]}")
        count += 1
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key in sorted(status_dicts.keys()):
        print(f"{key}: {status_dicts[key]}")
    raise

print(f"File size: {total_size}")
for key in sorted(status_dicts.keys()):
    print(f"{key}: {status_dicts[key]}")
