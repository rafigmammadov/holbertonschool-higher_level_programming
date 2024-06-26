#!/usr/bin/python3
"""
Module that contains convert_csv_to_json() function
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    Function that takes the CSV filename as its
    parameter and writes the JSON data to data.json
    """
    try:
        data = {}

        with open(filename, mode="r") as f:
            csv_lines = csv.DictReader(f)

            data = list(csv_lines)

        with open("data.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=4))
            return True

    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False
