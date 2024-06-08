#!/usr/bin/python3
"""
Module that contains print_statistics() function
"""
import sys
from collections import defaultdict


def print_statistics(total_size, status_counts):
    """
    Function that reads stdin line by line and computes metrics
    """
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")


def compute_metrics(lines):
    total_size = 0
    status_counts = defaultdict(int)

    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 8:
            status_code = parts[5]
            file_size = int(parts[7])
            total_size += file_size
            status_counts[status_code] += 1

    return total_size, status_counts


def main():
    lines = []
    try:
        for line in sys.stdin:
            lines.append(line)
            if len(lines) % 10 == 0:
                total_size, status_counts = compute_metrics(lines)
                print_statistics(total_size, status_counts)
                lines = []
    except KeyboardInterrupt:
        total_size, status_counts = compute_metrics(lines)
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    main()
