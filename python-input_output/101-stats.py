#!/usr/bin/python3
"""
Module that contains print_statistics() function
"""
import sys
from collections import defaultdict


def print_stats(total_size, status_code_counts):
    """
    Function that reads stdin line by line and computes metrics
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_code_counts):
        print("{}: {}".format(code, status_code_counts[code]))


if __name__ == "__main__":
    import sys

    accumulated_size = 0
    accumulated_status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_stats(accumulated_size, accumulated_status_codes)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                size = int(parts[-1])
                accumulated_size += size
            except (IndexError, ValueError):
                pass

            try:
                status_code = parts[-2]
                if status_code in valid_codes:
                    if status_code not in accumulated_status_codes:
                        accumulated_status_codes[status_code] = 1
                    else:
                        accumulated_status_codes[status_code] += 1
            except IndexError:
                pass

        print_stats(accumulated_size, accumulated_status_codes)

    except KeyboardInterrupt:
        print_stats(accumulated_size, accumulated_status_codes)
        raise
